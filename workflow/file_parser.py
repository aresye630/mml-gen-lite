#!/usr/bin/env python3
"""file_parser.py — 用户上传文件的通用解析器（纯代码，不调 LLM）。

★ 设计目标
  用户可上传任意文件（docx/xlsx/pdf/csv/txt/md/json/yaml...），
  统一转成 markdown 文本放 uploads_text/，agent 只读文本。

★ 为什么不做成 skill
  解析是确定性的（格式固定 → 转换规则固定），不需要 agent 判断。
  做成 skill 会让 agent 每次多读一次 SKILL.md，还容易调错参数。
  只有"解析结果不够用、要换策略"才需要 agent 判断，这写进 prompt 就够。

★ 目录约定
  /data/sessions/{sid}/uploads/        原始文件
  /data/sessions/{sid}/uploads_text/   解析后的 markdown
  /data/sessions/{sid}/uploads_index.json  索引（供 agent 和前端读）

★ 用法
  python3 file_parser.py --session <sid>             解析全部
  python3 file_parser.py --session <sid> --file x.docx  解析单个
"""
import argparse
import json
import os
import re
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

# 文本类直接读
TEXT_EXT = {'.txt', '.md', '.markdown', '.csv', '.tsv', '.json', '.yaml', '.yml',
            '.xml', '.log', '.conf', '.cfg', '.ini', '.mml', '.sql', '.py', '.sh'}
# 需要转换
DOC_EXT = {'.docx', '.doc'}
SHEET_EXT = {'.xlsx', '.xls', '.xlsm'}
PDF_EXT = {'.pdf'}


# ═══════════════════════════════════════════════════════════
# 单个格式的解析
# ═══════════════════════════════════════════════════════════
def parse_text(path):
    """纯文本直接读（尝试多种编码）。"""
    for enc in ('utf-8', 'gbk', 'gb18030', 'utf-16', 'latin-1'):
        try:
            return path.read_text(encoding=enc), {'encoding': enc}
        except (UnicodeDecodeError, LookupError):
            continue
    # 全失败：用 replace 兜底
    return path.read_text(encoding='utf-8', errors='replace'), {'encoding': 'utf-8(replace)'}


def parse_docx(path):
    """Word → markdown。保留标题层级、段落、表格。"""
    try:
        import docx
    except ImportError:
        raise RuntimeError('python-docx 未安装')

    d = docx.Document(str(path))
    out = []
    meta = {'paragraphs': 0, 'tables': 0}

    for block in d.element.body:
        tag = block.tag.split('}')[-1]
        if tag == 'p':
            # 段落
            texts = []
            for t in block.iter():
                if t.tag.endswith('}t') and t.text:
                    texts.append(t.text)
            txt = ''.join(texts).strip()
            if not txt:
                continue
            # 判断标题级别
            style = ''
            pPr = block.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pPr')
            if pPr is not None:
                pStyle = pPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pStyle')
                if pStyle is not None:
                    style = pStyle.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') or ''
            m = re.search(r'(?:Heading|heading)\s*(\d)', style)
            if m:
                out.append('#' * int(m.group(1)) + ' ' + txt)
            elif 'Title' in style:
                out.append('# ' + txt)
            else:
                out.append(txt)
            meta['paragraphs'] += 1
        elif tag == 'tbl':
            # 表格
            rows = []
            for tr in block.iter():
                if not tr.tag.endswith('}tr'):
                    continue
                cells = []
                for tc in tr.iter():
                    if not tc.tag.endswith('}tc'):
                        continue
                    cell_txt = ''.join(
                        t.text or '' for t in tc.iter() if t.tag.endswith('}t')
                    ).strip().replace('|', '\\|')
                    cells.append(cell_txt)
                if cells:
                    rows.append(cells)
            if rows:
                out.append('')
                out.append('| ' + ' | '.join(rows[0]) + ' |')
                out.append('|' + '---|' * len(rows[0]))
                for r in rows[1:]:
                    out.append('| ' + ' | '.join(r) + ' |')
                out.append('')
                meta['tables'] += 1

    return '\n'.join(out), meta


def parse_xlsx(path):
    """Excel → markdown 表格（每个 sheet 一节）。"""
    try:
        import openpyxl
    except ImportError:
        raise RuntimeError('openpyxl 未安装')

    wb = openpyxl.load_workbook(str(path), data_only=True)
    out = []
    meta = {'sheets': [], 'total_rows': 0}

    for ws in wb.worksheets:
        rows = []
        for row in ws.iter_rows(values_only=True):
            if all(c is None or str(c).strip() == '' for c in row):
                continue
            rows.append(['' if c is None else str(c).strip().replace('|', '\\|')
                         for c in row])
        if not rows:
            continue
        meta['sheets'].append({'name': ws.title, 'rows': len(rows)})
        meta['total_rows'] += len(rows)

        out.append(f'## Sheet: {ws.title}')
        out.append('')
        # 第一行当表头
        out.append('| ' + ' | '.join(rows[0]) + ' |')
        out.append('|' + '---|' * len(rows[0]))
        for r in rows[1:]:
            # 补齐列数
            r2 = r + [''] * (len(rows[0]) - len(r))
            out.append('| ' + ' | '.join(r2[:len(rows[0])]) + ' |')
        out.append('')

    wb.close()
    return '\n'.join(out), meta


def parse_pdf(path):
    """PDF → 文本。"""
    try:
        import pdfplumber
    except ImportError:
        raise RuntimeError('pdfplumber 未安装')

    out = []
    meta = {'pages': 0}
    with pdfplumber.open(str(path)) as pdf:
        meta['pages'] = len(pdf.pages)
        for i, page in enumerate(pdf.pages, 1):
            txt = page.extract_text() or ''
            if txt.strip():
                out.append(f'<!-- page {i} -->')
                out.append(txt)
            # 表格
            for tbl in (page.extract_tables() or []):
                if not tbl or not tbl[0]:
                    continue
                out.append('')
                out.append('| ' + ' | '.join(str(c or '').replace('|', '\\|') for c in tbl[0]) + ' |')
                out.append('|' + '---|' * len(tbl[0]))
                for r in tbl[1:]:
                    out.append('| ' + ' | '.join(str(c or '').replace('|', '\\|') for c in r) + ' |')
                out.append('')
    return '\n'.join(out), meta


def parse_doc_legacy(path):
    """老 .doc（二进制）→ 尝试 antiword/textutil。"""
    for cmd in (['antiword', str(path)], ['textutil', '-convert', 'txt', '-stdout', str(path)]):
        if not which(cmd[0]):
            continue
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout, {'tool': cmd[0]}
    raise RuntimeError('无法解析 .doc（缺 antiword/textutil）')


def which(name):
    from shutil import which as _w
    return _w(name)


# ═══════════════════════════════════════════════════════════
# 文件类型识别
# ═══════════════════════════════════════════════════════════
def sniff_type(path):
    """识别文件类型（扩展名优先，内容嗅探兜底）。"""
    ext = path.suffix.lower()

    # 扩展名明确
    if ext in DOC_EXT:
        return 'doc'
    if ext in SHEET_EXT:
        return 'sheet'
    if ext in PDF_EXT:
        return 'pdf'
    if ext in TEXT_EXT:
        return 'text'

    # 内容嗅探（无扩展名或扩展名不对）
    try:
        head = path.read_bytes()[:4096]
    except Exception:
        return 'unknown'

    if head.startswith(b'PK\x03\x04'):
        # zip 容器：看内部结构
        try:
            with zipfile.ZipFile(path) as z:
                names = z.namelist()
                if any(n.startswith('word/') for n in names):
                    return 'doc'
                if any(n.startswith('xl/') for n in names):
                    return 'sheet'
        except Exception:
            pass
    if head.startswith(b'%PDF'):
        return 'pdf'

    # 尝试当文本读
    try:
        head.decode('utf-8')
        return 'text'
    except UnicodeDecodeError:
        try:
            head.decode('gbk')
            return 'text'
        except UnicodeDecodeError:
            return 'binary'


def is_ml_exp(text):
    """判断文本是不是 MML EXP 快照（按命令密度）。"""
    if len(text) < 5000:
        return False
    hits = len(re.findall(r'^\s*(ADD|MOD|RMV|SET|DEL)\s+[A-Z]', text, re.M))
    return hits >= 20


# ═══════════════════════════════════════════════════════════
# 主流程
# ═══════════════════════════════════════════════════════════
def parse_one(src: Path, out_dir: Path):
    """解析单个文件，返回索引条目。"""
    entry = {
        'name': src.name,
        'size': src.stat().st_size,
        'kind': None,
        'parsed': None,
        'error': None,
        'notes': [],
        'meta': {},
    }
    try:
        kind = sniff_type(src)
        entry['kind'] = kind

        if kind == 'text':
            text, meta = parse_text(src)
            entry['meta'] = meta
        elif kind == 'doc':
            if src.suffix.lower() == '.doc':
                text, meta = parse_doc_legacy(src)
            else:
                text, meta = parse_docx(src)
            entry['meta'] = meta
            if meta.get('tables'):
                entry['notes'].append(f"{meta['tables']} 个表格已转为 markdown")
        elif kind == 'sheet':
            text, meta = parse_xlsx(src)
            entry['meta'] = meta
            if meta.get('sheets'):
                entry['notes'].append(
                    f"{len(meta['sheets'])} 个 sheet，共 {meta['total_rows']} 行")
        elif kind == 'pdf':
            text, meta = parse_pdf(src)
            entry['meta'] = meta
            entry['notes'].append(f"{meta.get('pages', 0)} 页")
        else:
            raise RuntimeError(f'不支持的文件类型: {kind}')

        # 判定是不是 EXP
        if kind == 'text' and is_ml_exp(text):
            n = len(re.findall(r'^\s*(ADD|MOD|RMV|SET|DEL)\s+[A-Z]', text, re.M))
            entry['role'] = 'exp'
            entry['notes'].append(f'识别为 MML 现网快照（{n} 条命令）')
        elif kind == 'text':
            entry['role'] = 'data'

        # 写解析结果
        out_name = src.stem + '.md'
        out_path = out_dir / out_name
        # 加个来源头，方便 agent 定位
        header = (f'<!-- 来源文件: {src.name} | 类型: {kind} | '
                  f'大小: {src.stat().st_size} B -->\n\n')
        out_path.write_text(header + text, encoding='utf-8')
        entry['parsed'] = out_name
        entry['chars'] = len(text)

    except Exception as e:
        entry['error'] = f'{type(e).__name__}: {e}'

    return entry


def build_index(sess_dir: Path):
    """扫描 uploads/ 生成索引。"""
    up = sess_dir / 'uploads'
    txt = sess_dir / 'uploads_text'
    up.mkdir(parents=True, exist_ok=True)
    txt.mkdir(parents=True, exist_ok=True)

    files = sorted(p for p in up.iterdir() if p.is_file() and not p.name.startswith('.'))
    entries = [parse_one(f, txt) for f in files]

    index = {
        'session': sess_dir.name,
        'updated_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'files': entries,
        'summary': {
            'total': len(entries),
            'ok': sum(1 for e in entries if not e['error']),
            'failed': sum(1 for e in entries if e['error']),
            'exp_count': sum(1 for e in entries if e.get('role') == 'exp'),
        },
    }
    (sess_dir / 'uploads_index.json').write_text(
        json.dumps(index, ensure_ascii=False, indent=1), encoding='utf-8')
    return index


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--session', required=True)
    ap.add_argument('--file', default=None, help='只解析指定文件')
    ap.add_argument('--data-root', default='/data/sessions')
    a = ap.parse_args()

    sess = Path(a.data_root) / a.session
    if not sess.exists():
        print(f'会话不存在: {sess}', file=sys.stderr)
        sys.exit(1)

    idx = build_index(sess)
    print(json.dumps(idx, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
