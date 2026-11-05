import os
# 在 sentence-transformers 导入前禁止 tokenizer 并行，避免 loky fork 冲突
os.environ.setdefault('TOKENIZERS_PARALLELISM', 'false')
os.environ.setdefault('OMP_NUM_THREADS', '1')

import warnings
import numpy as np

# 统一嵌入层：按后端可用性自动选择
#   MML_EMB_BACKEND=onnx   → onnxruntime（轻量，容器/目标环境默认）
#   MML_EMB_BACKEND=torch  → sentence-transformers（本机原行为）
#   MML_EMB_BACKEND=auto   → onnx 可用则 onnx，否则 torch（默认）
# 模型路径：MML_EMB_MODEL（默认本机 bge 目录；容器内 /opt/expgv/models/bge-small-zh-onnx）
_DEFAULT_MODEL = os.path.expanduser('~/workspace/models/bge-small-zh-v1.5-onnx')


def _resolve_backend():
    b = os.environ.get('MML_EMB_BACKEND', 'auto').lower()
    if b in ('onnx', 'torch'):
        return b
    # auto：优先 onnx（无 torch 依赖）
    try:
        import onnxruntime  # noqa: F401
        return 'onnx'
    except ImportError:
        return 'torch'


class Emb:
    """bge-small 嵌入统一入口。get_embeddings(str|list[str]) → np.ndarray(n,512)。"""

    def __init__(self, backend=None):
        self.backend = backend or _resolve_backend()
        self.model_dir = os.environ.get('MML_EMB_MODEL', _DEFAULT_MODEL)
        if self.backend == 'onnx':
            from get_embeddings_onnx import Emb as _OnnxEmb
            self._impl = _OnnxEmb(self.model_dir)
        else:
            from sentence_transformers import SentenceTransformer
            from joblib.externals import loky
            import atexit
            self._loky = loky
            self._model = SentenceTransformer(self.model_dir)
            atexit.register(self.cleanup)

    def get_embeddings(self, texts):
        if self.backend == 'onnx':
            return self._impl.get_embeddings(texts)
        # torch 后端：single=True 避免内部创建并行 pool
        return self._model.encode(texts, show_progress_bar=False)

    def cleanup(self):
        if self.backend == 'onnx':
            return self._impl.cleanup()
        try:
            # 先触发 gc 回收模型相关对象，减少 loky executor 引用
            import gc
            gc.collect()
            ex = self._loky.get_reusable_executor()
            if ex is not None:
                ex.shutdown(wait=True)
        except Exception:
            pass

    def __del__(self):
        self.cleanup()
