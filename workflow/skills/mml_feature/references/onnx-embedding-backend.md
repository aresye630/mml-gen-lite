# ONNX 轻量嵌入后端（无 torch）—— 容器/交付环境用（2026-09-12）

## 为什么需要

交付镜像要能在 arm64 Linux 跑通向量检索（配置生成链路依赖），但
`sentence-transformers` 依赖 `torch`。实测在 arm64 容器里 `pip install torch`
会连带拉 NVIDIA CUDA 包（`nvidia_cudnn_cu13` 651MB 等），构建 **OOM/超时失败**
（exit 137）。镜像从 1.44G 膨胀到预计 3~4G 也不可接受。

**结论：用 onnxruntime 替代 torch 跑 bge-small。** 依赖只剩
`onnxruntime + transformers(仅要 tokenizer) + numpy + jieba`，权重 ~95M。

## 导出（一次性，需 torch 环境）

`bge-small-zh-v1.5` 官方 `1_Pooling/config.json` 是 `pooling_mode_cls_token: true`
→ 用 **CLS pooling + L2 normalize** 包装 backbone：

```python
class W(nn.Module):
    def __init__(self, model): super().__init__(); self.model = model
    def forward(self, input_ids, attention_mask, token_type_ids):
        out = self.model(input_ids=input_ids, attention_mask=attention_mask,
                         token_type_ids=token_type_ids)
        return torch.nn.functional.normalize(out.last_hidden_state[:, 0], p=2, dim=1)

torch.onnx.export(W(model).eval(), (ids, mask, ttype), "model.onnx", opset_version=17,
    input_names=["input_ids","attention_mask","token_type_ids"],
    output_names=["embeddings"],
    dynamic_axes={k: {0:"b",1:"s"} for k in ("input_ids","attention_mask","token_type_ids")})
```

坑：
- **需要 `onnxscript`**（torch 2.12 的 `torch.onnx` 走 dynamo 导出，缺它 `ModuleNotFoundError`）。
  本机受 PEP 668 限制，建 venv 时要 `--system-site-packages` 才能复用系统的 torch/transformers。
- 导出时**必须用修正过的 tokenizer**（见下），否则参考值本身就是错的。
- 导出会有 `version_converter` 的 axes 断言告警，属噪声，导出仍成功（产物 514KB 图 + 95M 外部数据）。

## 推理侧

`get_embeddings_onnx.py`（与 `get_embeddings.py` API 兼容：`Emb(model_dir)` + `get_embeddings(texts)`）。

- `ort.SessionOptions()` 设 `intra/inter_op_num_threads = 1`（避免线程争抢）。
- 三个输入 `input_ids/attention_mask/token_type_ids` **都要喂**，即使模型不要求。
- `AutoTokenizer.from_pretrained(model_dir)` 即可 —— **前提是 tokenizer 已修**（见下）。

## ⚠ 必须先修 tokenizer，否则数值对不上（本次踩坑主线）

最初容器内验 ONNX vs torch 得到 `cos = 1.0`，但改用 **sentence-transformers 官方 encode
作 groundtruth** 后 `cos 只有 0.867`。逐层排查结论：

**模型目录 tokenizer 资产不自洽** —— `tokenizer.json` 的 `normalizer.lowercase=false`
且 `tokenizer_config.json` 的 `do_lower_case=false`，与 `vocab.txt`（小写 WordPiece：
`q`=159, `##os`=8470）矛盾：

| 加载方式 | 切分 "配置QoS覆盖" | 结果 |
|---|---|---|
| sentence-transformers（内部 WordPiece 小写化） | `[101,6981,5390,159,8470,6208,4667,102]` | 正确 |
| HF `AutoTokenizer.from_pretrained` | `[101,6981,5390,100,6208,4667,102]` | 100=[UNK] 错 |

**修复**：两处 lowercase 都置 `true`（脚本 `fix_bge_tokenizer_json.py`）。

排查过程中被排除的错误假设（记下省得重走）：
- ✗ pooling 不对 —— 实测 ST 加载出 `pooling_mode='cls'`，与官方配置一致；
- ✗ MPS/CPU 精度差 —— 两者 cos = 1.0；
- ✗ 权重/dtype 不同 —— 完全一致；
- ✗ 手工 `BertTokenizer(vocab_file=...)` 构造 —— 新版 transformers 慢速实现只读到 5 个
  特殊 token（`vocab_size=5`）全吐 UNK，**别用这条路**。

**验收标准**：ONNX vs ST 官方 `cos > 0.9999` 且 `max_abs_diff < 1e-6`。
修复后实测 `cos = 1.0`、`max_abs_diff = 2.2e-07` → PASS。

## 后端自动选择

`get_embeddings.py` 已加统一层：`MML_EMB_BACKEND = auto|onnx|torch`（默认 auto）——
模型目录有 `model.onnx` 就走 onnx，否则回退 torch。本机两者并存，行为不变；
容器内只有 onnx，自动走轻量路径。**本机回归**：hybrid_search 切换后端后
score 完全一致（0.0492 / 0.0323）。

## Docker Desktop 挂载坑

`/tmp` **不在 Docker Desktop 文件共享白名单**，`-v /tmp/xxx:/x` 挂进去是**空目录**
（不报错，静默空）。验证模型/脚本挂载请放 `~/workspace/...` 下。
另外镜像有 entrypoint 时，`docker run <img> python3 xxx.py` 会被 entrypoint 吞掉
→ 加 `--entrypoint python3`（`-u` 要放在 entrypoint 之后作为其参数）。
