#!/usr/bin/env python3
"""Second-brain intake, searchable extraction, queue rendering, and health checks."""

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
from datetime import datetime, timedelta
from pathlib import Path


VAULT = Path("/Users/mac/Documents/Obsidian Vault")
STATE = VAULT / "90-系统/收件系统/收件状态.json"
QUEUE = VAULT / "90-系统/收件系统/收件队列.json"
QUEUE_NOTE = VAULT / "00-知识库入口/待整理资料.md"
ATTACHMENTS = VAULT / "40-资料源/附件/待整理"
SOURCE_NOTES = VAULT / "40-资料源/待整理资料页"
ROOTS = [Path("/Users/mac/Desktop"), Path("/Users/mac/Documents"), Path("/Users/mac/Downloads")]

TEXT_EXTS = {".md", ".txt", ".csv"}
OFFICE_EXTS = {".docx", ".pdf", ".pptx", ".xlsx"}
LEGACY_OFFICE_EXTS = {".doc", ".ppt", ".xls"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".heic"}
AUDIO_EXTS = {".mp3", ".m4a", ".wav", ".aac", ".flac"}
VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".webm"}
SUPPORTED = TEXT_EXTS | OFFICE_EXTS | LEGACY_OFFICE_EXTS | IMAGE_EXTS | AUDIO_EXTS | VIDEO_EXTS

EXCLUDED_DIRS = {
    ".git", ".obsidian", ".venv", "venv", ".tox", "node_modules", "__pycache__", "qa",
    "Obsidian Vault", "Obsidian Vault整理备份", "docx_render_check", "docx_pdf_check",
}
EXCLUDED_PREFIXES = ("render", "qa_", "客户软件安装包_", "U盘备份_格式化前_")
EXCLUDED_FILES = {".DS_Store", "AGENTS.md", "README.md", "知识库投递说明.md"}
FINAL_HINTS = (
    "最终", "成品", "交付", "发布版", "专业版", "优化版", "方案", "手册", "报告", "清单",
    "逐字稿", "转写", "transcript", "课程", "访谈", "会议", "录音", "语音", "海报", "封面",
)
PRIVATE_PATTERNS = re.compile(r"(password|passwd|token|cookie|secret|api[_ -]?key|密码|密钥|验证码)", re.I)


def parse_args():
    parser = argparse.ArgumentParser(description="Operate the personal second-brain pipeline.")
    sub = parser.add_subparsers(dest="command", required=True)
    intake = sub.add_parser("intake")
    intake.add_argument("--since")
    intake.add_argument("--until")
    intake.add_argument("--dry-run", action="store_true")
    intake.add_argument("--max-copy-mb", type=int, default=100)
    sub.add_parser("process")
    sub.add_parser("health")
    sessions = sub.add_parser("session-sources")
    sessions.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"))
    return parser.parse_args()


def parse_time(value):
    dt = datetime.fromisoformat(value)
    if dt.tzinfo:
        dt = dt.astimezone().replace(tzinfo=None)
    return dt


def load_json(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, json.JSONDecodeError):
        return default


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def file_hash(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_excluded_dir(path):
    if path.name in EXCLUDED_DIRS or any(path.name.startswith(p) for p in EXCLUDED_PREFIXES):
        return True
    return (path / ".git").exists()


def is_candidate(path, start, end):
    if not path.is_file() or path.name in EXCLUDED_FILES or path.name.startswith((".", "~$")):
        return False, "系统或隐藏文件"
    try:
        path.relative_to(VAULT)
        return False, "知识库自身"
    except ValueError:
        pass
    if any(is_excluded_dir(parent) for parent in path.parents):
        return False, "排除目录"
    if path.suffix.lower() not in SUPPORTED:
        return False, "不支持格式"
    if PRIVATE_PATTERNS.search(path.name):
        return False, "疑似敏感文件"
    stat = path.stat()
    if stat.st_size == 0:
        return False, "空文件"
    modified = datetime.fromtimestamp(stat.st_mtime)
    if not start <= modified < end:
        return False, "窗口外"
    return True, "候选"


def trust_level(path):
    parts = set(path.parts)
    lower = path.name.lower()
    if "知识库投递" in parts:
        return "自动入库"
    if str(path).startswith("/Users/mac/Documents/Codex/") and "outputs" in parts:
        return "自动入库"
    if any(h.lower() in lower for h in FINAL_HINTS):
        return "自动入库"
    return "待确认"


def kind_for(ext):
    if ext in AUDIO_EXTS:
        return "音频"
    if ext in VIDEO_EXTS:
        return "视频"
    if ext in IMAGE_EXTS:
        return "图片"
    if ext in OFFICE_EXTS | LEGACY_OFFICE_EXTS:
        return "文档"
    return "文本"


def next_action(ext, copied):
    if not copied:
        return "确认是否入库"
    if ext in AUDIO_EXTS:
        return "待转写和讲者确认"
    if ext in VIDEO_EXTS:
        return "待建立稳定引用和文本说明"
    if ext in IMAGE_EXTS:
        return "待OCR或人工说明"
    if ext in LEGACY_OFFICE_EXTS:
        return "待转换为新版格式后提取文本"
    return "自动提取可搜索文本"


def unique_target(source):
    target = ATTACHMENTS / source.name
    if not target.exists():
        return target
    source_hash = file_hash(source)
    if file_hash(target) == source_hash:
        return target
    for i in range(2, 1000):
        alt = ATTACHMENTS / f"{source.stem}-{i}{source.suffix}"
        if not alt.exists() or file_hash(alt) == source_hash:
            return alt
    raise RuntimeError(f"cannot allocate target for {source}")


def entry_id(path, digest):
    return digest[:12] if digest else hashlib.sha256(str(path).encode()).hexdigest()[:12]


def initialize_existing(queue):
    known_paths = {item.get("vault_path") for item in queue}
    if not ATTACHMENTS.exists():
        return queue
    for path in sorted(ATTACHMENTS.iterdir()):
        if not path.is_file():
            continue
        rel = path.relative_to(VAULT).as_posix()
        if rel in known_paths:
            continue
        digest = file_hash(path)
        queue.append({
            "id": entry_id(path, digest), "received_at": datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds"),
            "name": path.name, "kind": kind_for(path.suffix.lower()), "extension": path.suffix.lower(),
            "source_path": "历史收件来源见待整理资料旧记录", "vault_path": rel, "sha256": digest,
            "trust": "历史已收件", "status": "待处理", "next_action": next_action(path.suffix.lower(), True),
            "note_path": "", "size_mb": round(path.stat().st_size / 1024 / 1024, 2), "related_project": "待判断",
        })
    return queue


def render_queue(queue):
    order = {"待处理": 0, "待确认": 1, "仅登记": 2, "待转写": 3, "待OCR": 4, "已结构化": 5, "不入库": 9}
    queue = sorted(queue, key=lambda x: (order.get(x.get("status"), 8), x.get("received_at", "")), reverse=False)
    counts = {}
    for item in queue:
        counts[item["status"]] = counts.get(item["status"], 0) + 1
    summary = "；".join(f"{k}{v}项" for k, v in sorted(counts.items())) or "当前没有待处理资料"
    lines = [
        "---", "title: 待整理资料", "type: system", "status: reviewed",
        "summary: 每日新增资料的唯一人工处理入口。", f"updated: {datetime.now().strftime('%Y-%m-%d')}",
        "topics:", "  - 收件", "  - 待整理", "related:", '  - "[[90-系统/收件系统/收件系统说明]]"', "---", "",
        "# 待整理资料", "", "> [!important]", "> 本页由收件队列生成。原件不因入库而删除；未形成可搜索文本的资料不算完成知识化。", "",
        "## 当前状态", "", f"{summary}。", "", "## 处理队列", "",
        "| 收件时间 | 资料 | 类型 | 来源级别 | 状态 | 下一步 | 关联项目 |", "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in queue:
        if item.get("note_path"):
            label = f"[[{item['note_path']}|{item['name']}]]"
        elif item.get("vault_path"):
            label = f"[[{item['vault_path']}|{item['name']}]]"
        else:
            label = f"`{item['name']}`"
        lines.append("| {received} | {label} | {kind} | {trust} | {status} | {action} | {project} |".format(
            received=item.get("received_at", "")[:16].replace("T", " "), label=label, kind=item.get("kind", ""),
            trust=item.get("trust", ""), status=item.get("status", ""), action=item.get("next_action", ""),
            project=item.get("related_project", "待判断"),
        ))
    lines += [
        "", "## 处理原则", "", "1. 先确认来源、隐私边界和关联项目。", "2. 音频先转写，图片先OCR或补说明，办公文件先提取文本。",
        "3. 资料页只记录来源事实；可复用结论另行进入知识层。", "4. 项目证据进入项目层，稳定步骤进入技能与SOP层。",
        "5. `待确认`项目只登记，不自动复制；确认无长期价值后标记`不入库`。", "",
        "[[00-知识库入口/知识库总览|返回知识底座]]", "",
    ]
    QUEUE_NOTE.write_text("\n".join(lines), encoding="utf-8")


def intake(args):
    state = load_json(STATE, {})
    start = parse_time(args.since) if args.since else parse_time(state.get("last_success_at", (datetime.now() - timedelta(days=1)).isoformat()))
    end = parse_time(args.until) if args.until else datetime.now()
    if start >= end:
        raise SystemExit("scan start must be before end")
    queue = initialize_existing(load_json(QUEUE, []))
    by_hash = {item.get("sha256"): item for item in queue if item.get("sha256")}
    by_source = {item.get("source_path"): item for item in queue}
    candidates = []
    skipped = {}
    for root in ROOTS:
        if not root.exists():
            continue
        for current, dirs, files in os.walk(root):
            current_path = Path(current)
            dirs[:] = [d for d in dirs if not is_excluded_dir(current_path / d)]
            for name in files:
                path = current_path / name
                ok, reason = is_candidate(path, start, end)
                if ok:
                    candidates.append(path)
                else:
                    skipped[reason] = skipped.get(reason, 0) + 1
    added = []
    for source in sorted(set(candidates), key=lambda p: str(p)):
        if str(source) in by_source:
            continue
        digest = file_hash(source)
        if digest in by_hash:
            continue
        ext = source.suffix.lower()
        trust = trust_level(source)
        size_mb = source.stat().st_size / 1024 / 1024
        copied = trust == "自动入库" and ext not in VIDEO_EXTS and size_mb <= args.max_copy_mb
        target = unique_target(source) if copied else None
        if copied and not args.dry_run:
            ATTACHMENTS.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                shutil.copy2(source, target)
        item = {
            "id": entry_id(source, digest), "received_at": datetime.now().isoformat(timespec="seconds"), "name": source.name,
            "kind": kind_for(ext), "extension": ext, "source_path": str(source),
            "vault_path": target.relative_to(VAULT).as_posix() if target else "", "sha256": digest, "trust": trust,
            "status": "待处理" if copied else ("仅登记" if trust == "自动入库" else "待确认"),
            "next_action": next_action(ext, copied), "note_path": "", "size_mb": round(size_mb, 2), "related_project": "待判断",
        }
        added.append(item)
        by_hash[digest] = item
    if not args.dry_run:
        queue.extend(added)
        save_json(QUEUE, queue)
        save_json(STATE, {"last_success_at": datetime.now().isoformat(timespec="seconds"), "updated_by": "second_brain_pipeline.py"})
        render_queue(queue)
    print(f"scan_start={start.isoformat(timespec='seconds')}")
    print(f"scan_end={end.isoformat(timespec='seconds')}")
    print(f"candidates={len(candidates)}")
    print(f"new_queue_items={len(added)}")
    for item in added:
        print(f"{item['status']}\t{item['kind']}\t{item['source_path']}")
    print("skipped=" + json.dumps(skipped, ensure_ascii=False, sort_keys=True))


def clean_text(value):
    return value.replace("\x00", "").strip()


def extract_text(path):
    ext = path.suffix.lower()
    if ext in {".md", ".txt"}:
        return path.read_text(encoding="utf-8", errors="replace")
    if ext == ".csv":
        return path.read_text(encoding="utf-8", errors="replace")
    if ext == ".docx":
        from docx import Document
        doc = Document(path)
        chunks = [p.text for p in doc.paragraphs if p.text.strip()]
        for table in doc.tables:
            for row in table.rows:
                chunks.append(" | ".join(cell.text.strip() for cell in row.cells))
        return "\n\n".join(chunks)
    if ext == ".pdf":
        from pypdf import PdfReader
        return "\n\n".join((page.extract_text() or "") for page in PdfReader(path).pages)
    if ext == ".pptx":
        from pptx import Presentation
        chunks = []
        for number, slide in enumerate(Presentation(path).slides, 1):
            text = [shape.text for shape in slide.shapes if hasattr(shape, "text") and shape.text.strip()]
            chunks.append(f"## 第{number}页\n\n" + "\n\n".join(text))
        return "\n\n".join(chunks)
    if ext == ".xlsx":
        from openpyxl import load_workbook
        wb = load_workbook(path, read_only=True, data_only=True)
        chunks = []
        for sheet in wb.worksheets:
            chunks.append(f"## 工作表：{sheet.title}")
            for index, row in enumerate(sheet.iter_rows(values_only=True), 1):
                if index > 1000:
                    chunks.append("[仅提取前1000行]")
                    break
                chunks.append(" | ".join("" if value is None else str(value) for value in row))
        return "\n".join(chunks)
    raise ValueError("format requires conversion or transcription")


def safe_title(name):
    title = re.sub(r"[\\/:*?\"<>|#\[\]]", "-", Path(name).stem).strip(" .-")
    return title[:80] or "未命名资料"


def create_source_note(item, text=""):
    SOURCE_NOTES.mkdir(parents=True, exist_ok=True)
    title = safe_title(item["name"])
    note = SOURCE_NOTES / f"{item['id']}-{title}.md"
    source_link = f"[[{item['vault_path']}|原始文件]]" if item.get("vault_path") else f"`{item['source_path']}`"
    searchable = bool(text.strip())
    processing = "已提取文本" if searchable else item["next_action"]
    body = [
        "---", f'title: "{title}"', "type: source", "status: raw", f'summary: "自动收件的{item["kind"]}资料，等待人工确认来源边界和知识价值。"',
        f"updated: {datetime.now().strftime('%Y-%m-%d')}", "topics:", "  - 待整理", f"source_file: \"{item.get('vault_path') or item['source_path']}\"",
        f"searchable: {'true' if searchable else 'false'}", f'processing: "{processing}"', "related: []", "---", "", f"# {title}", "",
        "> [!warning] 来源边界", "> 本页由收件系统自动生成，只表示资料已经保存或登记，不代表其中观点已经核验，也不代表用户立场。", "",
        "## 资料信息", "", f"- 类型：{item['kind']}", f"- 原始文件：{source_link}", f"- 原始来源：`{item['source_path']}`",
        f"- 收件时间：{item['received_at']}", f"- 当前处理：{processing}", "", "## 核心主线", "", "待人工或AI通读后补充。", "",
    ]
    if searchable:
        body += ["## 自动提取文本", "", clean_text(text), ""]
    else:
        body += ["## 待处理", "", f"- [ ] {item['next_action']}", "- [ ] 确认讲者、来源、时间和隐私边界", "- [ ] 形成可搜索文本后再提炼知识", ""]
    body += ["## 六要素提炼", "", "### 认知 / 观点", "", "### 方法论", "", "### 故事 / 数据", "", "### 情绪表达", "", "### 可发展选题", "", "### 待办", "", "## 分流结果", "", "- 知识：待判断", "- 项目证据：待判断", "- SOP或Skill：待判断", ""]
    note.write_text("\n".join(body), encoding="utf-8")
    return note.relative_to(VAULT).with_suffix("").as_posix(), searchable


def process_queue():
    queue = initialize_existing(load_json(QUEUE, []))
    changed = 0
    for item in queue:
        if item.get("note_path") or not item.get("vault_path"):
            continue
        path = VAULT / item["vault_path"]
        if not path.exists():
            item["status"] = "来源缺失"
            item["next_action"] = "核验原始文件和Vault副本"
            changed += 1
            continue
        try:
            text = extract_text(path)
        except Exception:
            text = ""
        note_path, searchable = create_source_note(item, text)
        item["note_path"] = note_path
        if searchable:
            item["status"] = "已结构化"
            item["next_action"] = "人工通读并决定是否提炼知识"
        elif item["extension"] in AUDIO_EXTS:
            item["status"] = "待转写"
        elif item["extension"] in IMAGE_EXTS:
            item["status"] = "待OCR"
        else:
            item["status"] = "待转换"
        changed += 1
    save_json(QUEUE, queue)
    render_queue(queue)
    print(f"processed={changed}")


def health():
    queue = load_json(QUEUE, [])
    counts = {}
    for item in queue:
        counts[item.get("status", "未知")] = counts.get(item.get("status", "未知"), 0) + 1
    last_review = None
    review_root = VAULT / "90-系统/04-Codex永久记忆/00-每日复盘"
    reviews = sorted(p for p in review_root.rglob("*.md") if p.name != "索引.md")
    if reviews:
        last_review = reviews[-1]
    files = [p for p in VAULT.rglob("*") if p.is_file()]
    rels = {p.relative_to(VAULT).as_posix() for p in files}
    stems = {p.relative_to(VAULT).with_suffix("").as_posix() for p in files}
    broken = []
    link_re = re.compile(r"\[\[([^\]]+)\]\]")
    for note in VAULT.rglob("*.md"):
        if note.relative_to(VAULT).parts[0] == "99-归档":
            continue
        for match in link_re.finditer(note.read_text(encoding="utf-8", errors="ignore")):
            raw = match.group(1).split("|", 1)[0].split("#", 1)[0].strip().lstrip("/")
            if not raw:
                continue
            candidates = [raw, raw + ".md", raw + ".base", (note.parent / raw).relative_to(VAULT).as_posix()]
            if not any(c in rels or c in stems for c in candidates):
                broken.append((note.relative_to(VAULT).as_posix(), raw))
    print("queue=" + json.dumps(counts, ensure_ascii=False, sort_keys=True))
    print(f"last_intake={load_json(STATE, {}).get('last_success_at', 'unknown')}")
    print(f"last_review={last_review.relative_to(VAULT) if last_review else 'none'}")
    print(f"active_broken_links={len(broken)}")
    for note, target in broken[:30]:
        print(f"BROKEN\t{note}\t{target}")


def session_sources(date_text):
    roots = [Path("/Users/mac/.codex/sessions"), Path("/Users/mac/.codex/archived_sessions")]
    matches = []
    for root in roots:
        if not root.exists():
            continue
        matches.extend(p for p in root.rglob("*.jsonl") if date_text in p.name or date_text.replace("-", "/") in str(p))
    print(f"date={date_text}")
    print(f"session_files={len(matches)}")
    for path in sorted(matches):
        print(path)


def main():
    args = parse_args()
    if args.command == "intake":
        intake(args)
    elif args.command == "process":
        process_queue()
    elif args.command == "health":
        health()
    elif args.command == "session-sources":
        session_sources(args.date)


if __name__ == "__main__":
    main()
