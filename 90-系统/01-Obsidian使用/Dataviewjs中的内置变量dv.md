---
tags:
  - obsidian
  - dataviewjs
created: 2026-07-07
---

# Dataviewjs 中的内置变量 dv

`dv` 是 DataviewJS 的入口对象，可以读取页面、输出表格、生成列表。

```dataviewjs
const pages = dv.pages('"03-产品与交付"')
  .sort(p => p.file.mtime, 'desc')
  .limit(10);

dv.table(["笔记", "修改时间"], pages.map(p => [p.file.link, p.file.mtime]));
```

常用方法：

- `dv.pages()`
- `dv.current()`
- `dv.table()`
- `dv.list()`
- `dv.paragraph()`
