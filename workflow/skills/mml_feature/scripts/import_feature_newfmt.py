#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""import_feature_newfmt.py — 新格式特性库 → Milvus 向量库导入器。

数据格式（~/Downloads/111 形态，2026-09-10 版本）：
  产品目录/UEG|UDG|UNC/**/*.md，每篇带 YAML frontmatter：
    name        特性名（中文）
    ne_type     产品（UEG/UDG/UNC）
    type        feature
    description 特性描述（中文，现成字段，无需从正文解析）
    doc_source  中文导航全路径（list；可能嵌套多路径 list[list]）
    risk_level  风险等级（可空）

  112 篇实测：全部含 frontmatter，3748 篇（UEG 2520 / UDG 514 / UNC 714）。

去重口径（2026-09-12 与用户确认）：
  同标题多副本 = 真实场景副本（如"配置N4接口"36 份实为 3 种描述×6 种正文，
  差异是部署场景：UEG-L/UPF 侧、主备热备/负荷分担/冷备）。doc_source 各不相同，
  去重会丢场景信息 → 全量入库，由检索侧按 doc_source 展示区分。

用法：
  python3 import_feature_newfmt.py --data_root ~/Downloads/111 --rebuild
  # env: MML_MILVUS_DIR / MML_EMB_MODEL / MML_EMB_BACKEND
"""
import argparse
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pymilvus import MilvusClient, DataType, Function, FunctionType  # noqa: E402
from get_embeddings import Emb  # noqa: E402

CLIENT_PATH = os.environ.get('MML_MILVUS_DIR',
                             os.path.expanduser('~/workspace/database/milvus_mml.db'))
COLLECTION_NAME = os.environ.get('MML_FEATURE_COLLECTION', 'mml_feature')
PRODUCTS = ('UEG', 'UDG', 'UNC')

_FM_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.S)
_DESC_MAX = 8000
_NAV_MAX = 8000
_NAME_MAX = 256
_PATH_MAX = 512

try:
    import yaml
except ImportError:
    yaml = None


def _norm_doc_source(ds):
    """doc_source 归一化为 list[str] 路径列表（展平嵌套）。"""
    if not ds:
        return []
    paths = []
    for item in (ds if isinstance(ds, list) else [ds]):
        if isinstance(item, (list, tuple)):
            paths.append(' > '.join(str(x) for x in item))
        else:
            paths.append(str(item))
    return paths


def parse_md(md_path: Path) -> dict | None:
    if yaml is None:
        raise RuntimeError('需要 pyyaml：pip install pyyaml')
    try:
        text = md_path.read_text(encoding='utf-8', errors='replace')
    except Exception:
        return None
    m = _FM_RE.match(text)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        return None

    name = str(fm.get('name', '')).strip()
    if not name:
        return None

    paths = _norm_doc_source(fm.get('doc_source'))
    # full_nav 用于展示与场景区分：取最具体的路径末段之前的部分
    # （末段通常等于特性名，无区分度；保留其上层导航链更有意义）
    if paths:
        seg = paths[-1].split(' > ')
        nav = ' > '.join(seg[:-1]) if len(seg) > 1 else paths[-1]
        nav = nav or paths[-1]
    else:
        nav = ''

    return {
        'feature_name': name[:_NAME_MAX],
        'feature_description': str(fm.get('description', '')).strip()[:_DESC_MAX],
        'full_nav': nav[:_NAV_MAX],
        'doc_source': ' | '.join(paths)[:_NAV_MAX],
        'product': str(fm.get('ne_type', '')).strip()[:64],
        'risk_level': str(fm.get('risk_level', '') or '').strip()[:64],
        'file_path': str(md_path)[:_PATH_MAX],
    }


class MMLFeatureDB:
    def __init__(self):
        self.client = MilvusClient(CLIENT_PATH)
        self.collection_name = COLLECTION_NAME

    def drop(self):
        if self.client.has_collection(self.collection_name):
            self.client.drop_collection(self.collection_name)
            print(f'[newfmt] 旧集合 {self.collection_name} 已删除')

    def _schema(self):
        s = self.client.create_schema(auto_id=False, enable_dynamic_field=True)
        s.add_field(field_name='id', is_primary=True, auto_id=True,
                    datatype=DataType.INT64)
        s.add_field(field_name='feature_name', datatype=DataType.VARCHAR,
                    max_length=512, enable_analyzer=True,
                    analyzer_params={'type': 'jieba'}, enable_match=True)
        s.add_field(field_name='feature_description', datatype=DataType.VARCHAR,
                    max_length=16384, enable_analyzer=True,
                    analyzer_params={'type': 'jieba'}, enable_match=True)
        s.add_field(field_name='full_nav', datatype=DataType.VARCHAR,
                    max_length=8192)
        s.add_field(field_name='doc_source', datatype=DataType.VARCHAR,
                    max_length=8192)
        s.add_field(field_name='product', datatype=DataType.VARCHAR, max_length=64)
        s.add_field(field_name='risk_level', datatype=DataType.VARCHAR, max_length=64)
        s.add_field(field_name='file_path', datatype=DataType.VARCHAR,
                    max_length=512)
        s.add_field(field_name='feature_name_dense',
                    datatype=DataType.FLOAT_VECTOR, dim=512)
        s.add_field(field_name='feature_description_dense',
                    datatype=DataType.FLOAT_VECTOR, dim=512)
        s.add_field(field_name='feature_name_sparse',
                    datatype=DataType.SPARSE_FLOAT_VECTOR)
        s.add_field(field_name='feature_description_sparse',
                    datatype=DataType.SPARSE_FLOAT_VECTOR)
        s.add_function(Function(
            name='feature_name_bm25', input_field_names=['feature_name'],
            output_field_names=['feature_name_sparse'],
            function_type=FunctionType.BM25))
        s.add_function(Function(
            name='feature_description_bm25',
            input_field_names=['feature_description'],
            output_field_names=['feature_description_sparse'],
            function_type=FunctionType.BM25))
        return s

    def _index(self):
        ip = self.client.prepare_index_params()
        for f in ('feature_name_dense', 'feature_description_dense'):
            ip.add_index(field_name=f, index_type='HNSW', metric_type='COSINE',
                         params={'M': 16, 'efConstruction': 200})
        for f in ('feature_name_sparse', 'feature_description_sparse'):
            ip.add_index(field_name=f, index_type='SPARSE_INVERTED_INDEX',
                         metric_type='BM25',
                         params={'inverted_index_algo': 'DAAT_MAXSCORE'})
        return ip

    def init(self):
        self.client.create_collection(collection_name=self.collection_name,
                                      schema=self._schema(),
                                      index_params=self._index())
        print(f'[newfmt] 集合 {self.collection_name} 已创建')

    def insert(self, recs, en, ed):
        rows = [{
            'feature_name': r['feature_name'],
            'feature_description': r['feature_description'],
            'full_nav': r['full_nav'],
            'doc_source': r['doc_source'],
            'product': r['product'],
            'risk_level': r['risk_level'],
            'file_path': r['file_path'],
            'feature_name_dense': [float(x) for x in a],
            'feature_description_dense': [float(x) for x in b],
        } for r, a, b in zip(recs, en, ed)]
        self.client.insert(self.collection_name, rows)
        return len(rows)

    def count(self):
        try:
            self.client.load_collection(self.collection_name)
            res = self.client.query(self.collection_name,
                                    output_fields=['count(*)'], limit=1)
            return res[0].get('count(*)') if res else 0
        except Exception as e:
            return f'count失败: {e}'


def iter_md(data_root: Path):
    """按产品目录遍历；产品取自目录名，缺失则从 fm.ne_type 兜底。"""
    for prod in PRODUCTS:
        d = data_root / prod
        if d.is_dir():
            for p in sorted(d.rglob('*.md')):
                yield prod, p


def main():
    ap = argparse.ArgumentParser(description='新格式特性库导入 Milvus')
    ap.add_argument('--data_root', required=True,
                    help='含 UEG/UDG/UNC 子目录的数据根（如 ~/Downloads/111）')
    ap.add_argument('--rebuild', action='store_true', help='删除旧集合重建')
    ap.add_argument('--batch', type=int, default=64)
    args = ap.parse_args()

    root = Path(args.data_root).expanduser().resolve()
    if not root.is_dir():
        sys.exit(f'目录不存在: {root}')

    db = MMLFeatureDB()
    if args.rebuild:
        db.drop()
        db.init()

    emb = Emb()
    print(f'[newfmt] embedding backend = {emb.backend}', flush=True)

    batch, total, skipped = [], 0, 0
    for prod, md in iter_md(root):
        rec = parse_md(md)
        if not rec:
            skipped += 1
            continue
        if not rec['product']:
            rec['product'] = prod
        batch.append(rec)
        if len(batch) >= args.batch:
            total += _flush(db, emb, batch)
            batch = []
    if batch:
        total += _flush(db, emb, batch)

    print(f'[newfmt] 导入完成 total={total} skipped={skipped} '
          f'库内计数={db.count()}', flush=True)
    emb.cleanup()


def _flush(db, emb, batch):
    en = emb.get_embeddings([r['feature_name'] for r in batch])
    ed = emb.get_embeddings([r['feature_description'] for r in batch])
    n = db.insert(batch, en, ed)
    print(f'  batch +{n}', flush=True)
    return n


if __name__ == '__main__':
    main()
