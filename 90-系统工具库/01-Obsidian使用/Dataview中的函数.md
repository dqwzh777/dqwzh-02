---
tags:
  - obsidian
  - dataview
created: 2026-07-07
---

# Dataview 中的函数

## 常用函数

- `date()`：处理日期
- `contains()`：判断是否包含某个值
- `length()`：计算列表长度
- `choice()`：条件选择
- `default()`：为空时使用默认值

## 示例

```dataview
TABLE default(status, "未标记") AS "状态"
FROM ""
WHERE contains(tags, "obsidian")
SORT file.mtime DESC
```
