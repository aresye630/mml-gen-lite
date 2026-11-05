# mml-gen-lite —— 极简 MML 配置生成系统
# 单镜像自带：后端 + workflow + 知识库 + 向量索引 + 嵌入模型 + 规则表
#
# 构建：
#   docker build -f dockerfiles/Dockerfile.workflow -t mml-gen-lite .
# 运行：
#   docker run -d -p 8600:8600 -e DEEPSEEK_API_KEY=xxx mml-gen-lite

FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple \
    DEBIAN_FRONTEND=noninteractive \
    TZ=Asia/Shanghai

# 国内镜像加速
RUN sed -i 's|deb.debian.org|mirrors.tuna.tsinghua.edu.cn|g' \
        /etc/apt/sources.list.d/*.sources 2>/dev/null || true

RUN apt-get update && apt-get install -y --no-install-recommends \
        curl ca-certificates xz-utils tini git procps \
    && rm -rf /var/lib/apt/lists/*

# 非 root 用户
RUN groupadd -g 1000 expgv \
    && useradd -u 1000 -g expgv -m -d /home/expgv -s /bin/bash expgv

# Python 依赖
COPY dockerfiles/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -f /tmp/requirements.txt

# ── 代码 ──────────────────────────────────────────────
COPY --chown=expgv:expgv backend/          /opt/expgv/backend/
COPY --chown=expgv:expgv workflow/         /opt/expgv/workflow/
COPY --chown=expgv:expgv scripts/          /opt/expgv/scripts/
COPY --chown=expgv:expgv rules/            /opt/expgv/rules/
COPY --chown=expgv:expgv tools/            /opt/expgv/tools/

# ── 知识库与模型 ──────────────────────────────────────
COPY kb/                                        /opt/expgv/kb/
COPY kb111/                                     /opt/expgv/kb111/
COPY models/bge-small-zh-v1.5-onnx              /opt/expgv/models/bge-small-zh-v1.5-onnx
COPY milvus-seed/                               /opt/expgv/milvus-seed/

# ── 运行环境 ──────────────────────────────────────────
ENV EXP_SESSIONS_ROOT=/data/sessions \
    WF_ROOT=/opt/expgv/workflow \
    MML_MILVUS_DIR=/opt/expgv/milvus-seed/milvus_mml.db \
    MML_EMB_MODEL=/opt/expgv/models/bge-small-zh-v1.5-onnx \
    MML_EMB_BACKEND=onnx \
    MML_DEFAULT_PRODUCT=UDG \
    EXP_TOOLS_DIR=/opt/expgv/tools \
    PORT=8600 \
    HERMES_SKIP_NODE_BOOTSTRAP=1

RUN mkdir -p /data/sessions \
    && chown -R expgv:expgv /data /opt/expgv

USER expgv
WORKDIR /opt/expgv

# hermes agent 运行时（配置模板在首次启动时由 entrypoint 展开）
COPY --chown=expgv:expgv dockerfiles/config.template.yaml /opt/expgv/config.template.yaml
RUN mkdir -p /home/expgv/.hermes/logs /home/expgv/.hermes/skills

EXPOSE 8600

HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
    CMD curl -fsS http://127.0.0.1:8600/health || exit 1

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/bin/sh", "-c", "bash /opt/expgv/scripts/entrypoint.sh"]
