#!/bin/bash
# entrypoint.sh —— 容器启动脚本
#
# 职责：
#   1. 从 config.template.yaml 展开环境变量（主要是 DEEPSEEK_API_KEY）到 ~/.hermes/config.yaml
#   2. 准备会话目录权限
#   3. 启动 app.py
set -e

CFG_TPL=/opt/expgv/config.template.yaml
CFG=/home/expgv/.hermes/config.yaml

# ── 1. 生成 hermes 配置 ──────────────────────────────
if [ ! -f "$CFG" ] || [ "$CFG_TPL" -nt "$CFG" ]; then
    echo "[entrypoint] 生成 hermes 配置"
    mkdir -p /home/expgv/.hermes
    # 只在模板里替换 API key，其他保持原样
    if [ -n "$DEEPSEEK_API_KEY" ]; then
        sed "s|\${DEEPSEEK_API_KEY}|$DEEPSEEK_API_KEY|g" "$CFG_TPL" > "$CFG"
    else
        echo "[entrypoint] ⚠ DEEPSEEK_API_KEY 未设置，agent 将无法调用模型"
        sed "s|\${DEEPSEEK_API_KEY}||g" "$CFG_TPL" > "$CFG"
    fi
    chmod 600 "$CFG"
fi

# ── 2. 会话目录 ──────────────────────────────────────
SESS=${EXP_SESSIONS_ROOT:-/data/sessions}
mkdir -p "$SESS"

# ── 3. 就绪检查 ──────────────────────────────────────
echo "[entrypoint] sessions=$SESS"
echo "[entrypoint] milvus=${MML_MILVUS_DIR:-未设置}"
echo "[entrypoint] model=${MML_EMB_MODEL:-未设置}"

if [ ! -d "${MML_MILVUS_DIR:-}" ]; then
    echo "[entrypoint] ⚠ 向量库不存在: ${MML_MILVUS_DIR}"
fi
if [ ! -d "${MML_EMB_MODEL:-}" ]; then
    echo "[entrypoint] ⚠ 嵌入模型不存在: ${MML_EMB_MODEL}"
fi

# ── 4. 启动 ──────────────────────────────────────────
echo "[entrypoint] 启动 app.py (port=${PORT:-8600})"
exec python /opt/expgv/backend/app.py
