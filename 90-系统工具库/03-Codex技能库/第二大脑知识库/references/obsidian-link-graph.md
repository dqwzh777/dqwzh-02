# Obsidian link-graph pattern

## Use case
When a user asks to connect new notes with existing vault content, treat the vault like a small graph, not isolated files.

## Pattern used in this session
- Create a concise "速览 / 首页" note for quick navigation.
- Keep a detailed canonical note for the full rules and background.
- Add bidirectional links between:
  - the quick overview note
  - the detailed note
  - the older legacy note(s)
  - the general vault index / usage note

## Practical steps
1. Identify the canonical node(s): detailed note, legacy note, global index.
2. Add a short overview note if the user wants an entry point.
3. Update related notes' "相关链接" / auto-links blocks in both directions.
4. Preserve existing content structure; prefer small link-only patches.
5. Verify by re-reading the updated files and confirming the links appear in each node.

## Pitfalls
- Don't create only one-way links; the graph should be navigable from new notes back to old notes.
- Don't treat the overview as a replacement for the detailed note; keep both.
- When a note has an AUTO-LINKS block, patch inside that block rather than rewriting unrelated sections.
