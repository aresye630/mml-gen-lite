#!/usr/bin/env python3
"""MML特性检索工具 - 支持语义检索和命令检索"""
import sys
sys.path = [p for p in sys.path if '/Library/Python/3.9' not in p]
import json
import logging
logging.disable(logging.CRITICAL)
import os
os.environ["TQDM_DISABLE"] = "1"
os.environ.setdefault('TOKENIZERS_PARALLELISM', 'false')
os.environ.setdefault('OMP_NUM_THREADS', '1')
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="jieba")
from pymilvus import MilvusClient, AnnSearchRequest, RRFRanker
import argparse
from get_embeddings import Emb

CLIENT_NAME = os.environ.get('MML_MILVUS_DIR', os.path.expanduser('~/workspace/database/milvus_mml.db'))
COLLECTION_NAME = 'mml_feature'

emb = Emb()

class MMLFeatureDB:
    def __init__(self, product="UEG"):
        self.client = MilvusClient(CLIENT_NAME)
        self.collection_name = COLLECTION_NAME
        self.product = product
        self._load_collections()

    def _load_collections(self):
        self.client.load_collection(collection_name=self.collection_name)

    def _make_filter(self):
        return f'product == "{self.product}"' if self.product else ''

    def search_by_semantic(self, text: str, top_k: int = 3):
        vec = emb.get_embeddings(text)
        flt = self._make_filter()
        name_dense_req = AnnSearchRequest(data=[vec], anns_field="feature_name_dense",
            param={"metric_type": "COSINE", "params": {"ef": 128}}, limit=top_k * 2, filter=flt)
        descrb_dense_req = AnnSearchRequest(data=[vec], anns_field="feature_description_dense",
            param={"metric_type": "COSINE", "params": {"ef": 128}}, limit=top_k * 2, filter=flt)
        name_sparse_req = AnnSearchRequest(data=[text], anns_field="feature_name_sparse",
            param={"metric_type": "BM25"}, limit=top_k * 2, filter=flt)
        descrb_sparse_req = AnnSearchRequest(data=[text], anns_field="feature_description_sparse",
            param={"metric_type": "BM25"}, limit=top_k * 2, filter=flt)
        ranker = RRFRanker(k=60)
        results = self.client.hybrid_search(
            collection_name=self.collection_name,
            reqs=[name_dense_req, name_sparse_req, descrb_dense_req, descrb_sparse_req],
            ranker=ranker, limit=top_k,
            output_fields=["full_nav", "file_path", "feature_name", "feature_description"]
        )
        final_results = []
        for hit in results[0]:
            # full_nav 在 mml_feature 库中为**纯文本**导航串（非 JSON）。
            # 包成单元素列表以保持下游 `for nav in r[0]` 的展示语义。
            full_nav = [hit["full_nav"]]
            with open(hit["file_path"], "r") as f:
                full_text = f.read()
            final_results.append((full_nav, full_text, hit["feature_name"], hit["feature_description"]))
        return final_results

    def search_by_feature_name(self, feature_name: str):
        filt = f'feature_name == "{feature_name}"'
        if self.product:
            filt += f' and product == "{self.product}"'
        results = self.client.query(
            collection_name=self.collection_name, filter=filt,
            output_fields=["full_nav", "file_path", "feature_name", "feature_description"], limit=100,
        )
        final_results = []
        for hit in results:
            full_nav = [hit["full_nav"]]
            with open(hit["file_path"], "r") as f:
                full_text = f.read()
            final_results.append((full_nav, full_text, hit["feature_name"], hit["feature_description"]))
        return final_results

def main():
    parser = argparse.ArgumentParser(description="MML特性检索工具")
    parser.add_argument("mode", choices=["semantic", "feature_name"], help="检索模式")
    parser.add_argument("query", type=str, help="待检索的文本")
    parser.add_argument("--top_k", type=int, nargs="?", default=5, help="【仅语义检索】返回条目数量")
    parser.add_argument("--product", default="UEG", help="产品筛选 (UEG/UDG/UNC)")
    args = parser.parse_args()

    db = MMLFeatureDB(product=args.product)

    if args.mode == "semantic":
        if args.top_k <= 0:
            parser.error("top_k 必须 > 0")
        results = db.search_by_semantic(args.query, args.top_k)
        if not results:
            print("未检索到结果，建议改写语义或者跟用户再确认")
        for i, r in enumerate(results):
            print(f"第{i}个结果：")
            print("feature_name:", r[2])
            print("feature_description:", r[3])
            print('-' * 20)
    elif args.mode == "feature_name":
        results = db.search_by_feature_name(args.query)
        if not results:
            print("未检索到结果，请确认特性名称是否输入正确")
        for i, r in enumerate(results):
            print(f"第{i}个结果：")
            print("全文内容：")
            print(r[1])
            print()
            print("完整导航目录：")
            for nav in r[0]:
                print(nav)
            print('-' * 20)

if __name__ == '__main__':
    main()
    emb.cleanup()
