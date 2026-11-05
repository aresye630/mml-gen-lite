#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""import_feature_v3.py — v3 新格式特性树 → Milvus 向量库导入器。

背景：v3 特性树（如 output_ueg_feature_v3）只有 .md、无 .json 元数据，
旧 import_feature_data.py 按 rglob('*.json') 读，对 v3 会导入 0 条。
本脚本按 v3 的实际结构解析：

  feature_name        ← md 首个一级标题 "# xxx"
  feature_description ← "## 操作场景" 段落正文（到下一个 "## " 为止）
  full_nav            ← 相对特性树根的目录路径（如 "kms/web/website"）
  file_path           ← md 绝对路径（供检索后回读全文）

实测（2026-09-12）：2343/2343 篇均含 "# 标题" 与 "## 操作场景"，解析无缺口。

用法：
  python3 import_feature_v3.py --product UEG \
      --data_dir ~/workspace/zhijian/output_ueg_feature/output_ueg_feature_v3 \
      --rebuild
  # 环境变量：MML_MILVUS_DIR / MML_EMB_MODEL / MML_EMB_BACKEND（见 get_embeddings.py）
"""
import argparse
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pymilvus import MilvusClient, DataType, Function, FunctionType  # noqa: E402
from get_embeddings import Emb  # noqa: E402

CLIENT_NAME = os.environ.get('MML_MILVUS_DIR',
                             os.path.expanduser('~/workspace/database/milvus_mml.db'))
COLLECTION_NAME = 'mml_feature'

_TITLE_RE = re.compile(r'^#\s+(.+?)\s*$', re.M)
# 任意层级标题（v3 里章节可能是 ## 或 ####，需同级/更高级都作为边界）
_ANY_HEAD_RE = re.compile(r'^(#{2,6})\s+(.+?)\s*$', re.M)
_SCENE_SECTION = '操作场景'
# 描述截断长度（与 v2 库字段容量一致；schema max_length=16384）
_DESC_MAX = 8000
# 导航用相对路径；VARCHAR(8192) 足够
_NAV_MAX = 8000


def parse_md(md_path: Path, root: Path) -> dict | None:
    """解析 v3 md → {feature_name, feature_description, full_nav, file_path}。"""
    try:
        text = md_path.read_text(encoding='utf-8', errors='replace')
    except Exception:
        return None

    m = _TITLE_RE.search(text)
    if not m:
        return None
    name = m.group(1).strip()

    # 描述：优先 "操作场景" 段（任意层级标题）；缺失则退化用标题后正文
    # 段落边界 = 同级或更高级标题（避免把 "#### 对系统的影响" 等后续章节并入）
    desc = ''
    heads = list(_ANY_HEAD_RE.finditer(text))
    for i, hd in enumerate(heads):
        if hd.group(2).strip() == _SCENE_SECTION:
            level = len(hd.group(1))
            start = hd.end()
            end = len(text)
            for nxt in heads[i + 1:]:
                if len(nxt.group(1)) <= level:
                    end = nxt.start()
                    break
            desc = text[start:end].strip()
            break
    if not desc:
        start = m.end()
        end = heads[0].start() if heads else len(text)
        desc = text[start:end].strip()

    # 去掉"版权所有"等尾注与多余空行
    desc = re.split(r'\n\s*版权所有', desc)[0].strip()
    desc = re.sub(r'\n{3,}', '\n\n', desc)

    rel = md_path.relative_to(root).parent
    nav = str(rel).replace(os.sep, '/')
    if nav == '.':
        nav = ''

    return {
        'feature_name': name[:128],
        'feature_description': desc[:_DESC_MAX],
        'full_nav': nav[:_NAV_MAX],
        'file_path': str(md_path),
    }


class MMLFeatureDB:
    def __init__(self):
        self.client = MilvusClient(CLIENT_NAME)
        self.collection_name = COLLECTION_NAME

    def del_collection(self):
        if self.client.has_collection(self.collection_name):
            self.client.drop_collection(self.collection_name)
            print(f'[v3] collection {self.collection_name} 已删除')

    def _create_schema(self):
        schema = self.client.create_schema(auto_id=False, enable_dynamic_field=True)
        schema.add_field(field_name='id', is_primary=True, auto_id=True,
                         datatype=DataType.INT64)
        schema.add_field(field_name='feature_name', datatype=DataType.VARCHAR,
                         max_length=128, enable_analyzer=True,
                         analyzer_params={'type': 'jieba'}, enable_match=True)
        schema.add_field(field_name='feature_description', datatype=DataType.VARCHAR,
                         max_length=16384, enable_analyzer=True,
                         analyzer_params={'type': 'jieba'}, enable_match=True)
        schema.add_field(field_name='full_nav', datatype=DataType.VARCHAR,
                         max_length=8192)
        schema.add_field(field_name='file_path', datatype=DataType.VARCHAR,
                         max_length=512)
        schema.add_field(field_name='product', datatype=DataType.VARCHAR,
                         max_length=64)
        schema.add_field(field_name='feature_name_dense',
                         datatype=DataType.FLOAT_VECTOR, dim=512)
        schema.add_field(field_name='feature_description_dense',
                         datatype=DataType.FLOAT_VECTOR, dim=512)
        schema.add_field(field_name='feature_name_sparse',
                         datatype=DataType.SPARSE_FLOAT_VECTOR)
        schema.add_field(field_name='feature_description_sparse',
                         datatype=DataType.SPARSE_FLOAT_VECTOR)
        schema.add_function(Function(
            name='feature_name_bm25', input_field_names=['feature_name'],
            output_field_names=['feature_name_sparse'], function_type=FunctionType.BM25))
        schema.add_function(Function(
            name='feature_description_bm25',
            input_field_names=['feature_description'],
            output_field_names=['feature_description_sparse'],
            function_type=FunctionType.BM25))
        return schema

    def _create_index(self):
        ip = self.client.prepare_index_params()
        ip.add_index(field_name='feature_name_dense', index_type='HNSW',
                     metric_type='COSINE', params={'M': 16, 'efConstruction': 200})
        ip.add_index(field_name='feature_description_dense', index_type='HNSW',
                     metric_type='COSINE', params={'M': 16, 'efConstruction': 200})
        ip.add_index(field_name='feature_name_sparse',
                     index_type='SPARSE_INVERTED_INDEX', metric_type='BM25',
                     params={'inverted_index_algo': 'DAAT_MAXSCORE'})
        ip.add_index(field_name='feature_description_sparse',
                     index_type='SPARSE_INVERTED_INDEX', metric_type='BM25',
                     params={'inverted_index_algo': 'DAAT_MAXSCORE'})
        return ip

    def init_collection(self):
        self.client.create_collection(
            collection_name=self.collection_name,
            schema=self._create_schema(),
            index_params=self._create_index())
        print(f'[v3] collection {self.collection_name} 已创建')

    def insert_batch(self, records, embs_name, embs_desc):
        rows = []
        for r, en, ed in zip(records, embs_name, embs_desc):
            rows.append({
                'feature_name': r['feature_name'],
                'feature_description': r['feature_description'],
                'full_nav': r['full_nav'],
                'file_path': r['file_path'],
                'product': r['product'],
                'feature_name_dense': [float(x) for x in en],
                'feature_description_dense': [float(x) for x in ed],
            })
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


def iter_md(data_dir: Path):
    for p in sorted(data_dir.rglob('*.md')):
        yield p


def main():
    ap = argparse.ArgumentParser(description='v3 特性树导入 Milvus')
    ap.add_argument('--product', default='UEG', help='UEG/UDG/UNC')
    ap.add_argument('--data_dir', required=True, help='v3 特性树目录')
    ap.add_argument('--rebuild', action='store_true', help='删除旧集合重建')
    ap.add_argument('--batch', type=int, default=64, help='批大小')
    args = ap.parse_args()

    root = Path(args.data_dir).expanduser().resolve()
    if not root.is_dir():
        sys.exit(f'目录不存在: {root}')

    db = MMLFeatureDB()
    if args.rebuild:
        db.del_collection()
        db.init_collection()

    emb = Emb()
    print(f'[v3] embedding backend = {emb.backend}', flush=True)

    batch, total, skipped = [], 0, 0
    for md in iter_md(root):
        rec = parse_md(md, root)
        if not rec:
            skipped += 1
            continue
        rec['product'] = args.product
        batch.append(rec)
        if len(batch) >= args.batch:
            total += _flush(db, emb, batch)
            batch = []
    if batch:
        total += _flush(db, emb, batch)

    print(f'[v3] 导入完成 total={total} skipped={skipped} '
          f'库内计数={db.count()}', flush=True)
    emb.cleanup()


def _flush(db, emb, batch):
    names = [r['feature_name'] for r in batch]
    descs = [r['feature_description'] for r in batch]
    en = emb.get_embeddings(names)
    ed = emb.get_embeddings(descs)
    n = db.insert_batch(batch, en, ed)
    print(f'  batch +{n} (累计 {n})', flush=True)
    return n


if __name__ == '__main__':
    main()
