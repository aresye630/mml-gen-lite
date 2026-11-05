#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""get_embeddings_onnx.py — bge-small 的 ONNX 轻量推理后端（无需 torch）。

与 get_embeddings.py（sentence-transformers/torch）API 完全兼容：
    emb = Emb(); vec = emb.get_embeddings("文本")   # 或 list[str]

模型目录需含：model.onnx + tokenizer.json + tokenizer_config.json
路径：MML_EMB_MODEL（默认 ~/workspace/models/bge-small-zh-v1.5-onnx，
      容器内为 /opt/expgv/models/bge-small-zh-onnx）

依赖：onnxruntime, transformers(tokenizer only), numpy —— 均无 torch。
"""
import os
import json
import numpy as np

os.environ.setdefault('TOKENIZERS_PARALLELISM', 'false')
os.environ.setdefault('OMP_NUM_THREADS', '1')

_DEFAULT_MODEL = os.path.expanduser('~/workspace/models/bge-small-zh-v1.5-onnx')


class Emb:
    """bge-small ONNX 嵌入（CLS pooling + L2 normalize，与官方一致）。"""

    def __init__(self, model_dir=None):
        import onnxruntime as ort

        self.model_dir = model_dir or os.environ.get('MML_EMB_MODEL', _DEFAULT_MODEL)
        onnx_path = os.path.join(self.model_dir, 'model.onnx')
        if not os.path.isfile(onnx_path):
            raise FileNotFoundError(f'ONNX 模型不存在: {onnx_path}')

        so = ort.SessionOptions()
        so.intra_op_num_threads = 1
        so.inter_op_num_threads = 1
        self.sess = ort.InferenceSession(
            onnx_path, sess_options=so, providers=['CPUExecutionProvider'])
        self.input_names = {i.name for i in self.sess.get_inputs()}
        self.tokenizer = self._load_tokenizer()

    def _load_tokenizer(self):
        """加载与 sentence-transformers 对齐的 tokenizer。

        ⚠ 关键坑：本模型目录的 tokenizer.json 原始 normalizer 为 lowercase=false，
        与 vocab.txt（小写 WordPiece）不自洽——会把 "QoS" 之类大写英文吐成 [UNK]。
        项目已用 fix_bge_tokenizer_json.py 修正为 lowercase=true（与 ST 内部
        WordPiece 默认行为一致），此处直接加载修正后的 tokenizer.json。
        若怀疑切分异常，先核对：tokenize("配置QoS覆盖") 应得
        [101, 6981, 5390, 159, 8470, 6208, 4667, 102]（无 100=UNK）。
        """
        from transformers import AutoTokenizer
        return AutoTokenizer.from_pretrained(self.model_dir)

    def get_embeddings(self, texts):
        """texts: str 或 list[str] → np.ndarray (n, 512)，float32，已 L2 归一。"""
        single = isinstance(texts, str)
        if single:
            texts = [texts]
        enc = self.tokenizer(texts, padding=True, truncation=True,
                             max_length=512, return_tensors='np')
        feed = {}
        if 'input_ids' in self.input_names:
            feed['input_ids'] = enc['input_ids'].astype(np.int64)
        if 'attention_mask' in self.input_names:
            feed['attention_mask'] = enc['attention_mask'].astype(np.int64)
        if 'token_type_ids' in self.input_names:
            tt = enc.get('token_type_ids')
            feed['token_type_ids'] = (tt.astype(np.int64) if tt is not None
                                      else np.zeros_like(enc['input_ids'], dtype=np.int64))
        out = self.sess.run(None, feed)[0]
        return out[0] if single else out

    def cleanup(self):
        pass

    def __del__(self):
        self.cleanup()
