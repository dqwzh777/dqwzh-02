---
name: second-brain-vault
description: Build and maintain a markdown second brain / Obsidian-style vault with a home page, linked child notes, and reusable templates.
platforms: [linux, macos, windows]
---

# Second Brain Vault Workflow

Use this skill when the user wants a note vault, Obsidian workspace, knowledge base, or a structured "second brain" made of markdown files.

## When to use
- Create or organize a vault home page
- Build linked child pages such as inbox, projects, notes, resources, tasks, and reviews
- Add or edit markdown notes inside an Obsidian vault
- Set up a reusable note-taking scaffold for future sessions

## Core workflow
1. Resolve the vault path first.
   - Prefer `OBSIDIAN_VAULT_PATH` if it is set.
   - If it is unset, use the conventional fallback `~/Documents/Obsidian Vault`.
   - Pass concrete absolute paths to file tools; do not leave shell variables unresolved.
2. Create the index/home page first.
   - Use a simple title, short purpose statement, and a few linked entry points.
3. Create the child pages next.
   - Typical starter set: `收集箱`, `项目`, `笔记`, `资料`, `待办`, `回顾`.
4. Keep each page focused.
   - Inbox pages collect raw material.
   - Project pages hold active work.
   - Note pages hold reusable knowledge.
   - Resource pages hold references and links.
   - Task pages hold actions.
   - Review pages hold reflection and retrospectives.
5. Maintain the link graph as you go.
   - Prefer a quick-entry note plus a detailed canonical note when the user is building a knowledge area.
   - Add bidirectional links between new notes, legacy notes, and the vault index so navigation works both ways.
   - When a note has an `AUTO-LINKS` block or a dedicated "相关链接" section, patch inside that block/section instead of rewriting the whole file.
6. Verify by reading the files back.
   - Confirm the created paths and that the content matches the intended structure.
   - Check that related pages link to each other, not only to the new page.

## Link graph workflow
- Prefer a hub-and-spoke pattern when adding a new knowledge area: one overview note, one quick-scan note if needed, and legacy pages that all point back to the hub.
- When a user wants "all new and old content connected", update both the new notes and the older README / index pages so the graph has reciprocal edges.
- Use short `相关链接` or `AUTO-LINKS` blocks as the insertion point for recurring maintenance.
- Keep duplicate headings out of markdown files; if a patch introduces one, clean it before finishing.
- If a file was previously read with pagination, re-read the whole file before overwriting it to avoid stale partial-view edits.

## Good defaults
- Prefer Chinese note titles if the user is working in Chinese.
- Use `[[wikilink]]` links on the home page and between related notes.
- Seed pages with small starter templates rather than empty files.
- Keep the home page editable; do not over-engineer it on the first pass.

## User-facing Obsidian deliverables

When saving management notes, inventories, or navigation aids into the user's Obsidian vault:

- Put the primary documents in the requested domain folder, but also create a short root-level index note when discoverability matters. The user often searches from Obsidian's quick switcher; a root note like `技能管理入口.md` is easier to find than a deeply nested folder.
- Distinguish clearly between Hermes skills and Obsidian plugins. A saved skill inventory is a markdown reference in the vault; it will not appear in Obsidian's plugin list.
- Preserve original English skill/tool names for searchability, but follow each English name or phrase with a Chinese translation in user-facing notes and summaries.
- After writing notes, verify by reading back the main entry note and listing the created files; then tell the user the exact vault-relative path and search term to open.

## Practical notes
- Use `read_file`, `write_file`, and `patch` for note operations.
- Use `search_files` to list notes or search content in the vault.
- If the user asks for a "second brain", start with the index page plus the six common child notes.
- See `references/obsidian-deliverables.md` for a compact checklist for saving Hermes outputs into an Obsidian vault.

## Verification checklist
- The vault path is concrete and absolute.
- The home page exists.
- The child notes exist and are linked from the home page.
- The notes contain usable starter content, not just blank stubs.

## Reference
- See `references/second-brain-structure.md` for a compact scaffold and layout guide.
- See `references/knowledge-base-linking.md` for the graph-linking pattern used when connecting new hub notes to the older vault structure.
- See `templates/second-brain-home.md` for a ready-to-copy home page starter.
