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
        curl ca-certificates xz-utils tini git procps libgomp1 \
    && rm -rf /var/lib/apt/lists/*
# ★ libgomp1：faiss-cpu 依赖的 OpenMP 运行库，缺了会报
#   ImportError: libgomp-xxx.so.1.0.0: cannot open shared object file

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

# ★ 2026-11-06：统一文件权限。
#   COPY 会把宿主机的权限带进镜像，实测有文件是 600（-rw-------），
#   别的用户/进程读不了，运行时 import 会失败。全部放开成 644 / 755。
RUN find /opt/expgv/backend /opt/expgv/workflow /opt/expgv/scripts \
         /opt/expgv/tools -type d -exec chmod 755 {} + \
 && find /opt/expgv/backend /opt/expgv/workflow /opt/expgv/scripts \
         /opt/expgv/tools -type f -exec chmod 644 {} + \
 && find /opt/expgv/scripts -name '*.sh' -exec chmod 755 {} +

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

# ── 预装 Node.js（必须，否则每次启动卡 10+ 分钟）────────────
# 本地缓存（可选）：把 node 文件夹放到项目根的 .node-cache，构建时自动使用
COPY .node-cache/ /tmp/node-dist/

# ★ 血泪教训（旧镜像踩过，重写时丢了，重新踩一遍）：
#   hermes 的 install.sh::check_node() **不检查 HERMES_SKIP_NODE_BOOTSTRAP**，
#   只检查 `command -v node` 和 `$HERMES_HOME/node/bin/node`。
#   两条都不满足就无条件 install_node → 内网下载 node22 tar.xz → 卡死。
#   而且安装日志会混进 stdout，污染 SSE 事件解析。
#   解法：构建期装好，运行期 shutil.which("node") 直接命中。
#
# 安装方式（二选一）：
#   A. 有本地缓存（推荐，离线可用）：把 node 目录放到 ../.build-cache/node，
#      构建时用 --build-arg NODE_CACHE=../.build-cache/node 不方便，
#      改为挂载：docker build --build-context nodecache=../.build-cache/node
#   B. 联网下载（镜像源：npmmirror，国内快）

# 先试本地缓存（通过 build context 传入，没有则联网下载）
ARG TARGETARCH=arm64
RUN set -eux; \
    mkdir -p /home/expgv/.hermes/node; \
    if [ -x /tmp/node-dist/bin/node ]; then \
      echo "使用本地 node 缓存"; \
      cp -a /tmp/node-dist/. /home/expgv/.hermes/node/; \
    else \
      echo "联网下载 node"; \
      case "$TARGETARCH" in \
        amd64) NODE_ARCH=x64 ;; \
        arm64) NODE_ARCH=arm64 ;; \
        *)     NODE_ARCH=$TARGETARCH ;; \
      esac; \
      NODE_VER=v22.23.4; \
      curl -fsSL --connect-timeout 30 --max-time 600 \
           "https://npmmirror.com/mirrors/node/${NODE_VER}/node-${NODE_VER}-linux-${NODE_ARCH}.tar.xz" \
           -o /tmp/node.tar.xz; \
      tar -xJf /tmp/node.tar.xz -C /tmp; \
      cp -a /tmp/node-${NODE_VER}-linux-${NODE_ARCH}/. /home/expgv/.hermes/node/; \
      rm -rf /tmp/node.tar.xz /tmp/node-${NODE_VER}-linux-${NODE_ARCH}; \
    fi; \
    ln -sf /home/expgv/.hermes/node/bin/node /usr/local/bin/node; \
    ln -sf /home/expgv/.hermes/node/bin/npm  /usr/local/bin/npm; \
    chmod -R a+rX /home/expgv/.hermes/node; \
    chmod 755 /home/expgv/.hermes/node/bin/node; \
    /home/expgv/.hermes/node/bin/node --version

# hermes agent 运行时目录（必须在 USER 切换前建，expgv 无权限 root 目录）
COPY --chown=expgv:expgv dockerfiles/config.template.yaml /opt/expgv/config.template.yaml
RUN mkdir -p /home/expgv/.hermes/logs /home/expgv/.hermes/skills \
    && chown -R expgv:expgv /home/expgv/.hermes

USER expgv
WORKDIR /opt/expgv

EXPOSE 8600

# ★ 2026-11-12 修：原来写死 8600，但容器可能用 -e PORT=862x 启动
#   导致健康检查永远失败（实测 fails=197，4 个容器全 unhealthy）
#   改为读环境变量 $PORT，缺省 8600
HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
    CMD curl -fsS "http://127.0.0.1:${PORT:-8600}/health" || exit 1

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/bin/sh", "-c", "bash /opt/expgv/scripts/entrypoint.sh"]
