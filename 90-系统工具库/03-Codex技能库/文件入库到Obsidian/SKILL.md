---
name: file-intake-to-obsidian
description: Scan local folders for meaningful, relatively complete files created or modified today and save them into the user's Obsidian inbox. Use when the user asks to入库, save useful files to Obsidian, check today's intake, prevent missing completed documents, or automatically archive completed plans, data, Markdown notes, Word/PDF/PowerPoint/Excel files, or reusable business materials.
---

# File Intake To Obsidian

## Purpose

Use this skill to keep the user's Obsidian vault as a curated knowledge base, not a dumping ground.

The rule is:

> Save meaningful, relatively complete, reusable files. Do not save loose chat fragments, temporary files, scripts, render previews, or one-off intermediate artifacts.

## Default Vault

Use this vault unless the user says otherwise:

`/Users/mac/Documents/Obsidian Vault`

Default inbox:

`/Users/mac/Documents/Obsidian Vault/00-首页与收件/收件箱`

## What To Intake

Intake files that are complete enough to reuse later:

- Word documents: `.docx`
- PDF documents: `.pdf`
- PowerPoint decks: `.pptx`
- Excel or spreadsheet files: `.xlsx`, `.csv`
- Complete Markdown notes: `.md`
- Meaningful image assets only when they are final business assets, not render previews: `.png`, `.jpg`, `.jpeg`

Prefer final deliverables, source Markdown for final deliverables, complete plans, complete training materials, questionnaires, SOPs, proposals, business data, customer diagnosis documents, and reusable conclusions.

## What To Exclude

Do not intake:

- Python, shell, JavaScript, or build scripts.
- Render-check pages like `page-1.png`.
- Folders named like `rendered_*`, `docx_pdf_check*`, `docx_render_check`, `*_render_check`, `ai_entry_ql`.
- `.DS_Store`, hidden files, caches, temporary files.
- Loose snippets or unfinished fragments.
- Existing files inside the Obsidian vault, except for updating the daily intake note.

## Workflow

1. Run `scripts/intake_to_obsidian.py`.
2. Review the printed summary.
3. If the user asked for automatic execution, accept the script's changes and report what was copied and where.
4. If the script copied nothing, explain whether there were no new qualifying files or whether the only candidates were excluded as temporary/intermediate.

## Script

Default command:

```bash
python3 /Users/mac/.codex/skills/file-intake-to-obsidian/scripts/intake_to_obsidian.py
```

Useful options:

```bash
python3 /Users/mac/.codex/skills/file-intake-to-obsidian/scripts/intake_to_obsidian.py --date 2026-07-09
python3 /Users/mac/.codex/skills/file-intake-to-obsidian/scripts/intake_to_obsidian.py --dry-run
python3 /Users/mac/.codex/skills/file-intake-to-obsidian/scripts/intake_to_obsidian.py --root "/path/to/project"
```

The script:

- Scans default roots: Desktop, Documents/AI入企计划, Documents/日常 2, Documents/AI视频.
- Copies qualifying files into `00-首页与收件/收件箱/附件/YYYY-MM-DD/`.
- Creates or updates `00-首页与收件/收件箱/YYYY-MM-DD-今日收件.md`.
- Adds one Obsidian wikilink per copied or already-present file.
- Avoids duplicate copying when the same target already exists with the same size.

## Final Response

Tell the user:

- Which date was processed.
- Which files were newly copied.
- Which files were already present.
- Which daily intake note was updated.
- Whether any likely candidates were skipped because they looked like temporary/intermediate files.
