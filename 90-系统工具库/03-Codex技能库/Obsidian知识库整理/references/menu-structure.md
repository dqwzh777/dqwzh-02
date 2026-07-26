# Obsidian menu-folder pattern

When the user wants the vault to behave like a collapsible menu tree in Obsidian, use folders as the primary navigation units and place a `首页.md` inside each folder.

## Pattern

- `第二大脑/` = top-level menu folder
- `第二大脑/首页.md` = main index page
- `第二大脑/收集箱/首页.md`, `第二大脑/项目/首页.md`, etc. = submenu pages

## Why this works

- Obsidian shows folders with disclosure arrows.
- A folder-based hierarchy is easier to browse than a flat list of notes.
- A `首页.md` inside each folder gives each menu item a landing page.

## Practical steps

1. Create the parent menu folder.
2. Move existing category notes into subfolders.
3. Rename or create each subfolder's landing note as `首页.md`.
4. Update wikilinks to point at folder landing pages, e.g. `[[收集箱/首页]]`.
5. Verify the filesystem tree with file tools.

## Pitfalls

- A markdown file named `收集箱.md` is still a file, not an expandable folder.
- If the user explicitly wants an arrow-based tree, do not leave the categories as flat sibling notes at the vault root.
- If you move notes into folders, keep the main index page in sync with the new paths.
