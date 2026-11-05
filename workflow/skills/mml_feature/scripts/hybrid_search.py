#!/usr/bin/env python3
"""
hybrid_search.py — 独立多查询混合检索脚本
支持多产品筛选。用法：
  python3 hybrid_search.py "查询1" "查询2" ...
  python3 hybrid_search.py --top_k 5 --product UDG "查询"
"""
import sys
import json
import os
import warnings
import argparse

os.environ['TOKENIZERS_PARALLELISM'] = 'false'
warnings.filterwarnings('ignore')

sys.path = [p for p in sys.path if '/Library/Python/3.9' not in p]
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from pymilvus import MilvusClient, AnnSearchRequest, RRFRanker
from get_embeddings import Emb

CLIENT_PATH = os.environ.get('MML_MILVUS_DIR', os.path.expanduser('~/workspace/database/milvus_mml.db'))
COLLECTION_NAME = 'mml_feature'


def hybrid_search(emb, client, query, top_k=3, product="UEG"):
    vec = emb.get_embeddings(query)
    flt = f'product == "{product}"' if product else ''

    name_dense = AnnSearchRequest(data=[vec], anns_field="feature_name_dense",
        param={"metric_type": "COSINE", "params": {"ef": 128}}, limit=top_k * 2, filter=flt)
    desc_dense = AnnSearchRequest(data=[vec], anns_field="feature_description_dense",
        param={"metric_type": "COSINE", "params": {"ef": 128}}, limit=top_k * 2, filter=flt)
    name_sparse = AnnSearchRequest(data=[query], anns_field="feature_name_sparse",
        param={"metric_type": "BM25"}, limit=top_k * 2, filter=flt)
    desc_sparse = AnnSearchRequest(data=[query], anns_field="feature_description_sparse",
        param={"metric_type": "BM25"}, limit=top_k * 2, filter=flt)

    results = client.hybrid_search(
        collection_name=COLLECTION_NAME,
        reqs=[name_dense, desc_dense, name_sparse, desc_sparse],
        ranker=RRFRanker(k=60), limit=top_k,
        output_fields=["full_nav", "feature_name", "feature_description"]
    )

    return [
        {
            "feature_name": hit["feature_name"],
            "score": round(hit["distance"], 4),
            "description": hit["feature_description"][:200] if hit["feature_description"] else "",
            "full_nav": hit["full_nav"][:150] if hit["full_nav"] else "",
        }
        for hit in results[0]
    ]


def main():
    parser = argparse.ArgumentParser(description="混合检索工具")
    parser.add_argument("--top_k", type=int, default=3, help="每个查询返回 Top-K 结果")
    parser.add_argument("--product", default="UEG", help="产品筛选 (UEG/UDG/UNC)")
    parser.add_argument("queries", nargs="+", help="查询语句")
    args = parser.parse_args()

    print(f"Loading model...", file=sys.stderr, flush=True)
    emb = Emb()
    client = MilvusClient(CLIENT_PATH)
    client.load_collection(COLLECTION_NAME)

    for q in args.queries:
        print(f"\n>>> {q}", file=sys.stderr, flush=True)
        results = hybrid_search(emb, client, q, args.top_k, args.product)
        out = {"query": q, "results": results, "product": args.product}
        print(json.dumps(out, ensure_ascii=False, indent=2))

    emb.cleanup()
    client.close()


if __name__ == '__main__':
    main()
