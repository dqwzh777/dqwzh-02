#!/usr/bin/env python3
import argparse
import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path


DEFAULT_VAULT = Path("/Users/mac/Documents/Obsidian Vault")
DEFAULT_ROOTS = [
    Path("/Users/mac/Desktop"),
    Path("/Users/mac/Documents/AI入企计划"),
    Path("/Users/mac/Documents/日常 2"),
    Path("/Users/mac/Documents/AI视频"),
]

GOOD_EXTS = {".docx", ".pdf", ".pptx", ".xlsx", ".csv", ".md"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg"}
EXCLUDE_DIR_PARTS = {
    ".git",
    ".obsidian",
    "node_modules",
    "__pycache__",
    "docx_render_check",
    "docx_pdf_check",
    "docx_pdf_check_v2",
    "docx_pdf_check_v3",
    "docx_pdf_check_v4",
    "docx_pdf_check_notables",
    "rendered_training_manual",
    "rendered_training_outline",
    "ai_entry_ql",
}
EXCLUDE_PREFIXES = ("rendered_",)
EXCLUDE_SUFFIXES = ("_render_check",)
EXCLUDE_FILE_PREFIXES = ("~$", ".")
EXCLUDE_NAMES = {".DS_Store"}
EXCLUDE_EXTS = {
    ".py",
    ".js",
    ".ts",
    ".sh",
    ".json",
    ".yaml",
    ".yml",
    ".log",
    ".tmp",
}
FINAL_IMAGE_HINTS = ("海报", "封面", "poster", "cover", "最终", "成品")


def parse_args():
    parser = argparse.ArgumentParser(description="Intake meaningful completed files into Obsidian inbox.")
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"), help="Date to process, YYYY-MM-DD.")
    parser.add_argument("--vault", default=str(DEFAULT_VAULT), help="Obsidian vault path.")
    parser.add_argument("--root", action="append", default=[], help="Extra root to scan. Can be repeated.")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without copying or editing notes.")
    return parser.parse_args()


def day_bounds(date_text):
    start = datetime.strptime(date_text, "%Y-%m-%d")
    return start, start + timedelta(days=1)


def is_excluded_dir(path):
    parts = set(path.parts)
    if parts & EXCLUDE_DIR_PARTS:
        return True
    return any(path.name.startswith(p) for p in EXCLUDE_PREFIXES) or any(path.name.endswith(s) for s in EXCLUDE_SUFFIXES)


def is_candidate_file(path, vault, start, end):
    if not path.is_file():
        return False, "not-file"
    if path.name in EXCLUDE_NAMES or path.name.startswith(EXCLUDE_FILE_PREFIXES):
        return False, "hidden-or-system"
    try:
        path.relative_to(vault)
        return False, "inside-vault"
    except ValueError:
        pass
    if any(is_excluded_dir(parent) for parent in path.parents):
        return False, "excluded-directory"
    ext = path.suffix.lower()
    if ext in EXCLUDE_EXTS:
        return False, "script-or-temp"
    if ext not in GOOD_EXTS and ext not in IMAGE_EXTS:
        return False, "unsupported-extension"
    if ext in IMAGE_EXTS and not any(h in path.name.lower() for h in FINAL_IMAGE_HINTS):
        return False, "image-not-final-asset"
    if path.name.lower().startswith("page-") and ext in IMAGE_EXTS:
        return False, "render-preview"
    mtime = datetime.fromtimestamp(path.stat().st_mtime)
    if not (start <= mtime < end):
        return False, "outside-date"
    if path.stat().st_size == 0:
        return False, "empty"
    return True, "candidate"


def unique_target(dest_dir, source):
    target = dest_dir / source.name
    if not target.exists():
        return target, False
    if target.stat().st_size == source.stat().st_size:
        return target, True
    stem, suffix = source.stem, source.suffix
    i = 2
    while True:
        alt = dest_dir / f"{stem}-{i}{suffix}"
        if not alt.exists():
            return alt, False
        if alt.stat().st_size == source.stat().st_size:
            return alt, True
        i += 1


def ensure_daily_note(inbox, date_text, dry_run):
    note = inbox / f"{date_text}-今日收件.md"
    if note.exists():
        return note
    content = "\n".join([
        "---",
        f"title: {date_text} 今日收件",
        f"date: {date_text}",
        "tags:",
        "  - inbox/daily",
        "status: collecting",
        "---",
        "",
        f"# {date_text} 今日收件",
        "",
        "## 待整理",
        "",
        "## 已处理",
        "",
    ])
    if not dry_run:
        note.write_text(content, encoding="utf-8")
    return note


def add_links(note, links, dry_run):
    if not links:
        return
    existing = note.read_text(encoding="utf-8") if note.exists() else ""
    new_lines = [line for line in links if line not in existing]
    if not new_lines or dry_run:
        return
    marker = "## 已处理"
    if marker in existing:
        before, after = existing.split(marker, 1)
        if before.rstrip().endswith("## 待整理"):
            updated = before.rstrip() + "\n\n" + "\n".join(new_lines) + "\n\n" + marker + after
        else:
            updated = before.rstrip() + "\n" + "\n".join(new_lines) + "\n\n" + marker + after
    else:
        updated = existing.rstrip() + "\n\n## 待整理\n\n" + "\n".join(new_lines) + "\n\n## 已处理\n"
    note.write_text(updated, encoding="utf-8")


def obsidian_link(vault, target):
    rel = target.relative_to(vault)
    display = target.name
    return f"- [[{rel.as_posix()}|{display}]]"


def main():
    args = parse_args()
    vault = Path(args.vault)
    inbox = vault / "00-Inbox 收件箱"
    dest_dir = inbox / "附件" / args.date
    start, end = day_bounds(args.date)
    roots = DEFAULT_ROOTS + [Path(r) for r in args.root]

    candidates = []
    skipped = {}
    for root in roots:
        if not root.exists():
            continue
        for current, dirs, files in os.walk(root):
            current_path = Path(current)
            dirs[:] = [d for d in dirs if not is_excluded_dir(current_path / d)]
            for name in files:
                path = current_path / name
                ok, reason = is_candidate_file(path, vault, start, end)
                if ok:
                    candidates.append(path)
                else:
                    skipped[reason] = skipped.get(reason, 0) + 1

    candidates = sorted(set(candidates), key=lambda p: (p.suffix.lower(), p.name))
    copied = []
    already = []
    links = []

    if not args.dry_run:
        dest_dir.mkdir(parents=True, exist_ok=True)
        inbox.mkdir(parents=True, exist_ok=True)

    for source in candidates:
        target, existed_same = unique_target(dest_dir, source)
        if existed_same:
            already.append(target)
        else:
            copied.append(target)
            if not args.dry_run:
                shutil.copy2(source, target)
        links.append(obsidian_link(vault, target))

    note = ensure_daily_note(inbox, args.date, args.dry_run)
    add_links(note, links, args.dry_run)

    print(f"date: {args.date}")
    print(f"vault: {vault}")
    print(f"daily_note: {note}")
    print(f"candidates: {len(candidates)}")
    print(f"copied: {len(copied)}")
    for item in copied:
        print(f"  COPIED {item}")
    print(f"already_present: {len(already)}")
    for item in already:
        print(f"  EXISTS {item}")
    interesting_skips = {k: v for k, v in skipped.items() if k in {"excluded-directory", "script-or-temp", "render-preview", "image-not-final-asset"}}
    if interesting_skips:
        print("skipped_summary:")
        for key, value in sorted(interesting_skips.items()):
            print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
