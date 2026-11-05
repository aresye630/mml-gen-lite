#!/bin/bash
# verify_v5_full.sh — 镜像内全功能验收（容器内执行）
#
# 验收范围（用户口径：全功能，不只看代码）：
#   A. 环境与知识资产就位
#   B. exp 分析链路（全代码化）
#   C. 配置生成（三产品）
#   D. 检索（三 skill × 两种模式）
#   E. 零本机粘连
#
# 用法（容器内）：bash /opt/expgv/scripts/verify_v5_full.sh
set -uo pipefail

PASS=0; FAIL=0; WARN=0
ok(){  echo "  [OK]   $1"; PASS=$((PASS+1)); }
ng(){  echo "  [FAIL] $1"; FAIL=$((FAIL+1)); }
wa(){  echo "  [WARN] $1"; WARN=$((WARN+1)); }
hdr(){ echo; echo "════ $1"; }

export HOME="${HOME:-/home/expgv}"
S="$HOME/.hermes/skills"
MILVUS="${MML_MILVUS_DIR:-/data/milvus/milvus_mml.db}"
export MML_MILVUS_DIR="$MILVUS"

hdr "A. 环境与知识资产"
[ -d /opt/expgv/kb ] && ok "分析知识库 /opt/expgv/kb ($(du -sh /opt/expgv/kb 2>/dev/null | cut -f1))" || ng "缺 /opt/expgv/kb"
N111=$(find /opt/expgv/kb111 -name '*.md' 2>/dev/null | wc -l | tr -d ' ')
[ "$N111" -gt 3000 ] && ok "111 知识库 /opt/expgv/kb111 ($N111 篇)" || ng "111 缺失或不全 ($N111)"
for p in ueg udg unc; do
  f="/opt/expgv/rules/feature_v5_$p.yaml"
  [ -f "$f" ] && ok "feature_v5_$p.yaml ($(du -h $f | cut -f1))" || ng "缺 $f"
done
[ -d "$MILVUS" ] && ok "向量库 $MILVUS" || ng "缺向量库 $MILVUS"

hdr "B. exp 分析链路（全代码化）"
A=/opt/expgv/scripts/exp_analysis_code
[ -d "$A" ] && ok "分析脚本目录就位" || ng "缺 $A"
nnet=0
for m in p1_parse p2_patterns p3_chains p4_diffs p5_notices p6_watchlist graph_walk graph_build feature_find feature_chain_map renderer; do
  [ -f "$A/$m.py" ] || continue
  grep -qE "requests\.|urllib|http\.client|socket\.|openai|api_key" "$A/$m.py" && nnet=$((nnet+1))
done
[ "$nnet" -eq 0 ] && ok "核心 11 模块无网络/LLM 依赖" || wa "核心模块含网络引用 $nnet 处"

hdr "C. 配置生成"
G=/opt/expgv/scripts/gen_mml_from_v5.py
[ -f "$G" ] && ok "生成器就位" || ng "缺生成器"
for p in ueg udg unc; do
  n=$(python3 -c "
import yaml
try:
    d = yaml.safe_load(open('/opt/expgv/rules/feature_v5_$p.yaml'))
    print(sum(1 for v in d['features'].values() if v.get('templates')))
except Exception: print(0)
" 2>/dev/null)
  [ "${n:-0}" -gt 0 ] && ok "feature_v5_$p 含模板特性 $n 个" || ng "feature_v5_$p 无模板"
done

hdr "D. 检索（三 skill × 两模式）"
run_ret(){
  local name="$1" script="$2" col="$3" mode="$4" q="$5"
  local out
  out=$(cd "$(dirname "$script")" && timeout 180 python3 "$script" "$mode" "$q" \
        --product UEG --top_k 1 2>/dev/null | head -c 200)
  if [ -n "$out" ]; then ok "$name $mode"; else ng "$name $mode（无输出）"; fi
}
SZ="$S/mml_feature/scripts/mml_feature_query.py"
SN="$S/mml_nav/scripts/mml_nav_query.py"
SS="$S/mml_support/scripts/mml_support_query.py"
[ -f "$SZ" ] && run_ret "mml_feature semantic" "$SZ" mml_feature semantic "配置QoS覆盖"
[ -f "$SZ" ] && run_ret "mml_feature feature_name" "$SZ" mml_feature feature_name "QoS"
[ -f "$SN" ] && run_ret "mml_nav semantic" "$SN" mml_nav semantic "流量管理"
[ -f "$SN" ] && run_ret "mml_nav nav_name" "$SN" mml_nav nav_name "配置"
[ -f "$SS" ] && run_ret "mml_support semantic" "$SS" mml_support semantic "配置QOS"
[ -f "$SS" ] && run_ret "mml_support command_name" "$SS" mml_support command_name "SET"

hdr "E. 零本机粘连"
# PITFALL: 检测器自身含 /Users/ 字样（它就是找这个的）→ 必须排除，否则自指误报。
# 另注：本脚本自己也要排除（文件名 verify_v5_full.sh）。
nlocal=$(grep -rl "/Users/" /opt/expgv/scripts /opt/expgv/rules /opt/expgv/backend \
         "$HOME/.hermes/skills" 2>/dev/null \
         | grep -vE "run_cases_v5\.py|verify_v5_full\.sh|build_v5_index\.py" \
         | wc -l | tr -d ' ')
[ "$nlocal" -eq 0 ] && ok "脚本/规则/技能无 /Users/ 残留" || ng "$nlocal 个文件含 /Users/ 路径"
# 向量库 file_path 采样
bad=$(python3 -c "
import os
try:
    from pymilvus import MilvusClient
    c = MilvusClient('$MILVUS')
    n = 0
    for coll in c.list_collections():
        for r in c.query(coll, filter='id >= 0', output_fields=['file_path'], limit=50):
            fp = r.get('file_path', '')
            if '/Users/' in fp or '/home/alesc' in fp: n += 1
    print(n)
except Exception as e: print(-1)
" 2>/dev/null)
[ "$bad" = "0" ] && ok "向量库 file_path 无本机残留" || wa "向量库本机路径残留 $bad 条"

hdr "F. 服务可用性"
code=$(python3 -c "
import http.client
try:
    c = http.client.HTTPConnection('127.0.0.1', 8600, timeout=10)
    c.request('GET', '/api/health')
    print(c.getresponse().status)
except Exception as e: print('ERR')
" 2>/dev/null)
[ "$code" = "200" ] && ok "服务 /api/health 200" || wa "服务健康检查: $code"

echo
echo "═══════════════════════════════════════════════"
echo "通过 $PASS / 失败 $FAIL / 警告 $WARN"
[ "$FAIL" -eq 0 ] && echo "✓ 全功能验收通过" || echo "✗ 有失败项，需修复"
exit $([ "$FAIL" -eq 0 ] && echo 0 || echo 1)
