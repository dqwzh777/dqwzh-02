---
name: obsidian-vault-organization
description: Organize an Obsidian vault into a collapsible folder-based menu with landing pages.
platforms: [linux, macos, windows]
---

# Obsidian Vault Organization

Use this skill when the user wants Obsidian to behave like a navigable menu tree rather than a flat pile of notes.

This skill complements the general `obsidian` skill by focusing on vault structure, folder navigation, and homepage-style landing pages.

## When to use

- The user wants a main menu / dashboard note for the vault.
- The user wants expandable arrow-style folders in Obsidian.
- The user wants section pages like 收集箱, 项目, 笔记, 资料, 待办, 回顾.
- The user is converting flat notes into folder-based navigation.

## Core pattern

- Create one top-level menu folder.
- Put a `首页.md` file inside the menu folder.
- Put each category into its own subfolder.
- Put a `首页.md` inside each category folder.
- Link from the menu page using wikilinks like `[[收集箱/首页]]`.

## Recommended workflow

1. Inspect the existing vault tree first.
2. Decide whether the user wants a flat note index or folder arrows.
3. If they want arrows, create folders, not sibling notes.
4. Move or rename existing category notes into folder landing pages.
5. Update the main index so it points at the new paths.
6. Verify the resulting filesystem layout before telling the user it is done.

## Pitfalls

- A file named `收集箱.md` is still a file; it does not create a collapsible menu.
- If the user explicitly asks for arrow navigation, avoid leaving the categories as flat root-level notes.
- Keep links in sync after moving files into folders.
- Folder structures should be reflected in the index page, not just in filenames.

## Support files

- `references/menu-structure.md` — concise recipe for the menu-folder pattern and verification steps.
