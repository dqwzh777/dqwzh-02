# Obsidian Deliverables Checklist

Use this reference when saving Hermes outputs into an Obsidian vault for the user.

## Checklist

1. Resolve the active vault path from `~/Library/Application Support/obsidian/obsidian.json` when possible; otherwise ask or use the configured vault path.
2. Save the detailed artifact in the requested folder, such as `skills/00-技能管理/` for skill inventories.
3. Add a short root-level index note when the artifact is important to find later. Use a plain Chinese title the user can search, for example `技能管理入口.md`.
4. In the index note, include wiki links to the detailed files and the absolute path for troubleshooting.
5. Explain that markdown notes saved in Obsidian are references, not Obsidian plugins or Hermes runtime skill installations.
6. Preserve exact English skill/tool names for search and execution, but place Chinese translations immediately after English names in user-facing text.
7. Verify by reading back the entry note and listing the created files before reporting completion.

## Suggested entry-note template

```markdown
# <中文入口标题>

这里是 <主题> 的入口页。

## 直接打开
- [[path/to/detail|详细文件]]

## 文件实际位置
`/absolute/vault/path/path/to/detail.md`

## 说明
这些是给用户查看和管理的 Markdown 参考文档，不是 Obsidian 插件。若是 Hermes skill 清单，真正可调用的 Hermes skill 安装在 `~/.hermes/skills`。
```
