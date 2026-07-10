---
tags:
  - obsidian
  - dataview
created: 2026-07-07
---

# Dataview 语法

## 常用查询

```dataview
TABLE file.mtime AS "修改时间", tags AS "标签"
FROM ""
SORT file.mtime DESC
LIMIT 20
```

## 按文件夹查询

```dataview
LIST
FROM "01-AI入企业务库"
SORT file.name ASC
```

## 按标签查询

```dataview
TABLE file.link AS "笔记"
FROM #obsidian
SORT file.mtime DESC
```
