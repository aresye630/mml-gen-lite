#!/usr/bin/env bash
# run_smoke.sh — v5 冒烟集统一入口（容器内执行）
#
# 用法:
#   bash run_smoke.sh                      # 跑全部（含 selftest）
#   bash run_smoke.sh --sid <id>           # 指定会话（必填，或用环境变量 SID）
#   bash run_smoke.sh --groups ABCDE       # 跑既有 5 组 + F/G/H
#   bash run_smoke.sh --selftest-only      # 只跑判别力自检
#   bash run_smoke.sh --quick              # 快速模式（跳过 agent 真调）
#
# 组说明:
#   A~E  既有 25 条（exp 代码 / 检索 / agent / 生成 / 交付）
#   F    会话与生成链路（CSV/版本链/状态一致/批量/下载/错误质量）   ← 新增
#   G    产物质量与三产品（非空/引号/分布/检索）                    ← 新增
#   H    体验与入口（对话通道/噪音/冗余入口/内部计数）               ← 新增
#
# 铁律:
#   1. 先跑 selftest —— 断言无判别力则整套不可信，直接退出
#   2. 组内失败不中断（由各自脚本保证）
#   3. 结果落盘到 /tmp/smoke_out/
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT="${SMOKE_OUT:-/tmp/smoke_out}"
SID="${SID:-}"
BASE="${SMOKE_BASE:-http://localhost:8600}"
GRPS="F G H"
QUICK=0
SELFTEST_ONLY=0

while [ $# -gt 0 ]; do
  case "$1" in
    --sid) SID="$2"; shift 2 ;;
    --base) BASE="$2"; shift 2 ;;
    --groups) GRPS="$2"; shift 2 ;;
    --selftest-only) SELFTEST_ONLY=1; shift ;;
    --quick) QUICK=1; shift ;;
    *) echo "未知参数: $1"; exit 2 ;;
  esac
done

# 去除组名中的分隔符（支持 "FGH" / "F G H" / "F,G,H"）
GRPS="$(echo "$GRPS" | tr -d ' ,')"

# 检索脚本需显式解释器（stdin 模式下 sys.executable 可能为空）
export SMOKE_PY="${SMOKE_PY:-$(command -v python3)}"

mkdir -p "$OUT"
echo "=========================================================="
echo " v5 冒烟集  base=$BASE  sid=${SID:-<未指定>}"
echo "=========================================================="

# ── 0. 判别力自检（必跑）──
echo
echo "--- 判别力自检（smoke_selftest）---"
python3 "$HERE/smoke_selftest.py"
ST=$?
if [ $ST -ne 0 ]; then
  echo
  echo "!! 自检未通过 —— 断言无判别力，整套结果不可信。中止。"
  exit 1
fi
if [ "$SELFTEST_ONLY" = "1" ]; then
  exit 0
fi

# ── 1. 既有 25 条（A~E）──
if [[ "$GRPS" == *"A"* ]] || [[ "$GRPS" == *"E"* ]]; then
  echo
  echo "--- 既有用例 A~E ---"
  if [ -f "$HERE/../run_cases_v5.py" ]; then
    python3 "$HERE/../run_cases_v5.py" --group ABCDE --json "$OUT/cases_abcde.json"
  else
    echo "  (跳过：未找到 ../run_cases_v5.py)"
  fi
fi

# ── 2. F 组：链路 ──
if [[ "$GRPS" == *"F"* ]]; then
  echo
  echo "--- F 组：会话与生成链路 ---"
  if [ -z "$SID" ]; then
    echo "  (跳过：未指定 --sid)"
  else
    python3 "$HERE/smoke_f_api.py" --base "$BASE" --sid "$SID" --json "$OUT/smoke_f.json"
  fi
fi

# ── 3. G 组：产物质量 ──
if [[ "$GRPS" == *"G"* ]]; then
  echo
  echo "--- G 组：产物质量与三产品 ---"
  if [ -z "$SID" ]; then
    echo "  (跳过：未指定 --sid)"
  else
    python3 "$HERE/smoke_g_quality.py" --sid "$SID" --json "$OUT/smoke_g.json"
  fi
fi

# ── 4. H 组：体验（真调 agent，quick 模式跳过）──
if [[ "$GRPS" == *"H"* ]]; then
  echo
  echo "--- H 组：体验与入口 ---"
  if [ -z "$SID" ]; then
    echo "  (跳过：未指定 --sid)"
  elif [ "$QUICK" = "1" ]; then
    echo "  (quick 模式：只跑静态项 H4/H5/H6)"
    python3 "$HERE/smoke_h_experience.py" --base "$BASE" --sid "$SID" \
      --only H4,H5,H6 --json "$OUT/smoke_h.json"
  else
    python3 "$HERE/smoke_h_experience.py" --base "$BASE" --sid "$SID" --json "$OUT/smoke_h.json"
  fi
fi

# ── 汇总 ──
echo
echo "=========================================================="
echo " 结果落盘目录: $OUT"
ls -1 "$OUT" 2>/dev/null | sed 's/^/   /'
echo "=========================================================="
