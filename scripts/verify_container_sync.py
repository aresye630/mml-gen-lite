#!/usr/bin/env python3
"""容器 vs 工作区代码对齐校验。

★ 2026-11-12（用户要求："确保是所有的改动都已经包含，不要出现不对齐的情况"）

之前踩过的坑：
  · docker cp 后忘记重启进程 → 验的是旧模块
  · 只拷了改动文件，漏了同批次其它文件
  · 镜像构建时 COPY 的目录和实际改动的目录不一致

校验策略：
  1. 文件清单对比：工作区每个 .py/.yaml 在容器里都存在？
  2. 内容 MD5 对比：逐文件哈希一致？
  3. 4 个容器之间也互相对比（防止某个容器漏更新）
  4. 关键模块可导入 + 版本标记

判据：全部一致才通过，任何不一致都列出来。
"""
import hashlib
import subprocess
import sys
from pathlib import Path

PROJ = Path('/Users/alesc/workspace/mml-gen-lite')
CONTAINERS = ['mmlgen-clean', 'mmlgen-b1', 'mmlgen-b2', 'mmlgen-b3']

# 要校验的目录（Dockerfile 里 COPY 的代码目录）
CHECK_DIRS = ['backend', 'workflow', 'scripts', 'rules', 'tools']

# 要跳过的（本地缓存、pyc、测试产物）
SKIP_PATTERNS = ('__pycache__', '.pyc', '.DS_Store', '.pytest_cache')

# 校验脚本自身不进镜像（构建后才写，属预期差异）
SELF_EXCLUDE = {'scripts/verify_container_sync.py'}


def list_files(root, base):
    """列出目录下所有文件（相对路径）。"""
    out = set()
    d = root / base
    if not d.exists():
        return out
    for p in d.rglob('*'):
        if not p.is_file():
            continue
        rel = p.relative_to(root)
        if any(s in str(rel) for s in SKIP_PATTERNS):
            continue
        if str(rel) in SELF_EXCLUDE:
            continue
        out.add(str(rel))
    return out


def md5_file(p):
    try:
        return hashlib.md5(Path(p).read_bytes()).hexdigest()
    except Exception:
        return None


def md5_in_container(cont, path):
    r = subprocess.run(
        ['docker', 'exec', '-u', 'expgv', cont, 'md5sum', path],
        capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        return None
    return r.stdout.split()[0] if r.stdout else None


def main():
    print('=' * 96)
    print('容器 vs 工作区代码对齐校验')
    print('=' * 96)

    # ── 1. 文件清单 ──
    print('\n【1】文件清单对比')
    local_files = set()
    for d in CHECK_DIRS:
        local_files |= list_files(PROJ, d)
    print(f'  工作区文件数: {len(local_files)}')

    for cont in CONTAINERS:
        missing = []
        for rel in local_files:
            r = subprocess.run(
                ['docker', 'exec', '-u', 'expgv', cont, 'test', '-f',
                 f'/opt/expgv/{rel}'],
                capture_output=True, timeout=30)
            if r.returncode != 0:
                missing.append(rel)
        status = '✅' if not missing else '❌'
        print(f'  {status} {cont}: {"全部存在" if not missing else f"缺 {len(missing)} 个"}')
        for m in missing[:5]:
            print(f'      {m}')

    # ── 2. 内容 MD5 对比 ──
    print('\n【2】内容 MD5 对比（逐文件）')
    mismatched = {c: [] for c in CONTAINERS}
    n_ok = 0
    for rel in sorted(local_files):
        # 只校验文本代码文件（跳过二进制）
        if rel.endswith(('.pyc', '.so', '.bin', '.db', '.faiss')):
            continue
        local_md5 = md5_file(PROJ / rel)
        if not local_md5:
            continue
        all_match = True
        for cont in CONTAINERS:
            cont_md5 = md5_in_container(cont, f'/opt/expgv/{rel}')
            if cont_md5 != local_md5:
                mismatched[cont].append(rel)
                all_match = False
        if all_match:
            n_ok += 1

    total_checked = sum(1 for r in local_files
                        if not r.endswith(('.pyc', '.so', '.bin', '.db', '.faiss')))
    print(f'  一致: {n_ok}/{total_checked} 文件')
    for cont in CONTAINERS:
        bad = mismatched[cont]
        status = '✅' if not bad else '❌'
        print(f'  {status} {cont}: {"全部一致" if not bad else f"{len(bad)} 个不一致"}')
        for b in bad[:8]:
            print(f'      {b}')
        if len(bad) > 8:
            print(f'      ... 还有 {len(bad)-8} 个')

    # ── 3. 容器之间互相对比 ──
    print('\n【3】4 个容器互相一致')
    # 选几个关键文件对比
    KEY_FILES = [
        'workflow/agent_run.py',
        'workflow/mcp/mcp_exp.py',
        'workflow/guard/guard.py',
        'workflow/guard/plan_wildcard.py',
        'workflow/mml_gen.py',
        'workflow/stage3/orchestrator.py',
        'workflow/stage3/biz_cluster.py',
        'workflow/stage3/attr_fill.py',
        'workflow/stage3/consistency.py',
        'workflow/stage3/copy_chain.py',
    ]
    for rel in KEY_FILES:
        md5s = {}
        for cont in CONTAINERS:
            md5s[cont] = md5_in_container(cont, f'/opt/expgv/{rel}')
        uniq = {v for v in md5s.values() if v}
        status = '✅' if len(uniq) == 1 and None not in md5s.values() else '❌'
        print(f'  {status} {rel}: {"一致" if len(uniq)==1 else f"{len(uniq)} 种哈希"}')

    # ── 4. 关键模块可导入 ──
    print('\n【4】关键模块可导入')
    TEST = '''
import sys
sys.path.insert(0, "/opt/expgv/workflow")
try:
    import mml_gen
    print("mml_gen OK")
except Exception as e:
    print(f"mml_gen FAIL: {e}")

sys.path.insert(0, "/opt/expgv/workflow/mcp")
for m in ["mcp_exp"]:
    try:
        __import__(m)
        print(f"{m} OK")
    except Exception as e:
        print(f"{m} FAIL: {e}")

sys.path.insert(0, "/opt/expgv/workflow/guard")
for m in ["guard", "plan_wildcard"]:
    try:
        __import__(m)
        print(f"{m} OK")
    except Exception as e:
        print(f"{m} FAIL: {e}")

sys.path.insert(0, "/opt/expgv/workflow/stage3")
for m in ["biz_cluster", "auto_ref", "ref_validate", "plan_check",
          "attr_fill", "consistency", "copy_chain", "orchestrator"]:
    try:
        __import__(m)
        print(f"{m} OK")
    except Exception as e:
        print(f"{m} FAIL: {e}")
'''
    for cont in CONTAINERS[:1]:   # 只测一个容器即可
        r = subprocess.run(['docker', 'exec', '-u', 'expgv', cont,
                            'python3', '-c', TEST],
                           capture_output=True, text=True, timeout=180)
        for line in r.stdout.strip().split('\n'):
            if line:
                mark = '✅' if 'OK' in line else '❌'
                print(f'  {mark} {line}')
        if r.stderr.strip():
            print(f'  stderr: {r.stderr[:300]}')

    # ── 5. EXP 工具数量（确认 mcp_exp 是四层重写版）──
    print('\n【5】exp 工具完整性（四层重写 + 新增工具）')
    TEST2 = '''
import sys
sys.path.insert(0, "/opt/expgv/workflow/mcp")
import mcp_exp
tools = [t["name"] for t in mcp_exp.TOOLS]
print("工具数:", len(tools))
print("工具:", ",".join(tools))
'''
    r = subprocess.run(['docker', 'exec', '-u', 'expgv', CONTAINERS[0],
                        'python3', '-c', TEST2],
                       capture_output=True, text=True, timeout=120)
    print(f'  {r.stdout.strip()[:400]}')
    if r.stderr.strip():
        print(f'  stderr: {r.stderr[:200]}')

    # ── 汇总 ──
    print('\n' + '=' * 96)
    total_bad = sum(len(v) for v in mismatched.values())
    if total_bad == 0:
        print('✅ 全部对齐')
        return 0
    print(f'❌ 有 {total_bad} 处不一致，需要修')
    return 1


if __name__ == '__main__':
    sys.exit(main())
