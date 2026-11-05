#!/usr/bin/env python3
"""MML特性数据导入脚本 — 支持多产品"""
import os
import sys
sys.path = [p for p in sys.path if '/Library/Python/3.9' not in p]
sys.path.insert(0, os.environ.get('MML_SCRIPTS_DIR', os.path.expanduser('~/.hermes/skills/mml_feature/scripts')))
import json
import argparse
from pathlib import Path
from pymilvus import MilvusClient, DataType, Function, FunctionType
from mylogger import get_logger
from get_embeddings import Emb

CLIENT_NAME = os.environ.get('MML_MILVUS_DIR', os.path.expanduser('~/workspace/database/milvus_mml.db'))
COLLECTION_NAME = 'mml_feature'
DEFAULT_DATA_DIR = os.environ.get('MML_FEATURE_DATA_DIR', os.path.expanduser('~/workspace/zhijian/output_ueg_feature/output_ueg_feature_v3'))

logger = get_logger(__name__)
emb = Emb()


class MMLFeatureDB:
    def __init__(self):
        self.client = MilvusClient(CLIENT_NAME)
        self.collection_name = COLLECTION_NAME

    def del_collection(self):
        if self.client.has_collection(self.collection_name):
            self.client.drop_collection(self.collection_name)
            logger.info(f"collection: {self.collection_name} 已删除")

    def _create_schema(self):
        schema = self.client.create_schema(auto_id=False, enable_dynamic_field=True)
        schema.add_field(field_name="id", is_primary=True, auto_id=True, datatype=DataType.INT64)
        schema.add_field(field_name="feature_name", datatype=DataType.VARCHAR, max_length=128,
                         enable_analyzer=True, analyzer_params={"type": "jieba"}, enable_match=True)
        schema.add_field(field_name="feature_description", datatype=DataType.VARCHAR, max_length=16384,
                         enable_analyzer=True, analyzer_params={"type": "jieba"}, enable_match=True)
        schema.add_field(field_name="full_nav", datatype=DataType.VARCHAR, max_length=8192)
        schema.add_field(field_name="file_path", datatype=DataType.VARCHAR, max_length=256)
        schema.add_field(field_name="product", datatype=DataType.VARCHAR, max_length=64)
        schema.add_field(field_name="feature_name_dense", datatype=DataType.FLOAT_VECTOR, dim=512)
        schema.add_field(field_name="feature_description_dense", datatype=DataType.FLOAT_VECTOR, dim=512)
        schema.add_field(field_name="feature_name_sparse", datatype=DataType.SPARSE_FLOAT_VECTOR)
        schema.add_field(field_name="feature_description_sparse", datatype=DataType.SPARSE_FLOAT_VECTOR)
        schema.add_function(Function(
            name="feature_name_bm25", input_field_names=['feature_name'],
            output_field_names=['feature_name_sparse'], function_type=FunctionType.BM25,
        ))
        schema.add_function(Function(
            name="feature_description_bm25", input_field_names=['feature_description'],
            output_field_names=['feature_description_sparse'], function_type=FunctionType.BM25,
        ))
        return schema

    def _create_index(self):
        index_params = self.client.prepare_index_params()
        index_params.add_index(field_name="feature_name_dense", index_type="HNSW", metric_type="COSINE",
                               params={"M": 16, "efConstruction": 256})
        index_params.add_index(field_name="feature_description_dense", index_type="HNSW", metric_type="COSINE",
                               params={"M": 16, "efConstruction": 256})
        index_params.add_index(field_name="feature_name_sparse", index_type="SPARSE_INVERTED_INDEX",
                               metric_type="BM25", params={"drop_ratio_build": 0.2})
        index_params.add_index(field_name="feature_description_sparse", index_type="SPARSE_INVERTED_INDEX",
                               metric_type="BM25", params={"drop_ratio_build": 0.2})
        return index_params

    def init_collection(self):
        schema = self._create_schema()
        index_params = self._create_index()
        self.client.create_collection(
            collection_name=self.collection_name,
            schema=schema,
            index_params=index_params
        )
        logger.info(f"collection: {self.collection_name} 创建成功")

    def batch_insert_datas(self, datas):
        feature_name_embs = emb.get_embeddings([d['feature_name'] for d in datas])
        feature_description_embs = emb.get_embeddings([d['feature_description'] for d in datas])
        insert_datas = []
        for i, data in enumerate(datas):
            insert_datas.append({
                "feature_name": data["feature_name"],
                "feature_description": data["feature_description"],
                "feature_name_dense": feature_name_embs[i],
                "feature_description_dense": feature_description_embs[i],
                "full_nav": json.dumps(data["full_nav"]),
                "file_path": data["file_path"],
                "product": data["product"],
            })
        self.client.insert(self.collection_name, insert_datas)
        logger.info(f"insert datas: {len(insert_datas)}")


def get_full_navs(nav_list):
    full_navs = []
    for navs in nav_list:
        full_nav = ''
        for nav in navs:
            full_nav += rf'{nav["name"]}\\\\'
        full_navs.append(full_nav[:-2])
    return full_navs


def batch_load_data(directory, batch_size=100, product="UEG"):
    path = Path(directory)
    batch = []
    for json_file in sorted(path.rglob('*.json')):
        md_file = Path(str(json_file.with_suffix("")) + ".md")
        if not md_file.is_file():
            logger.warning(f"md file: {md_file} 找不到，跳过")
            continue
        with open(json_file) as f:
            data = json.load(f)
        batch.append({
            "feature_name": data["feature_name"],
            "feature_description": data["feature_description"],
            "full_nav": get_full_navs(data["full_nav"]),
            "file_path": str(md_file),
            "product": product,
        })
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MML Feature 数据导入")
    parser.add_argument("--product", default="UEG", help="产品名称 (UEG/UDG/UNC)")
    parser.add_argument("--data_dir", default=DEFAULT_DATA_DIR, help="数据目录路径")
    parser.add_argument("--rebuild", action="store_true", help="删除旧集合重建")
    args = parser.parse_args()

    db = MMLFeatureDB()
    if args.rebuild:
        print("Step 1: Deleting old collection...")
        db.del_collection()
        print("Step 2: Creating new collection...")
        db.init_collection()
    print(f"Step 3: Importing data from {args.data_dir} (product={args.product})...")
    total = 0
    for idx, datas in enumerate(batch_load_data(args.data_dir, 100, args.product)):
        db.batch_insert_datas(datas)
        total += len(datas)
        print(f"  Batch {idx+1}: inserted {len(datas)} records (total: {total})")
    print(f"\nDone! Total records imported: {total}")

    emb.cleanup()
    print("Cleanup: loky executor shut down.")
