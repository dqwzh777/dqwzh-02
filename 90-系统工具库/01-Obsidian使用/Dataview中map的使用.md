---
tags:
  - obsidian
  - dataview
created: 2026-07-07
---

# Dataview 中 map 的使用

`map()` 用来把列表里的每一项转换成新的形式。

```dataview
TABLE map(file.tags, (t) => replace(t, "#", "")) AS "标签"
FROM ""
WHERE file.tags
LIMIT 20
```

适合用在标签清洗、字段转换、批量展示等场景。
