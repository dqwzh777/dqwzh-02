---
name: codex-chat-export
description: 导出 Codex / Codex App 本地会话记录为 Markdown 文件。读取本地 ~/.codex/sessions/ 与 ~/.codex/archived_sessions/ 中的 JSONL 会话,让用户选择日期或会话并导出为可读的 Markdown。适用场景:用户要求"导出聊天""导出对话""export""导出聊天记录""导出对话历史"等。
---

# Skill:导出 Codex 聊天记录

> 用途:把 Codex / Codex App 本地会话记录整理成可读 Markdown,方便复盘、沉淀课程素材、整理客户项目过程。

## 一飞版说明

这个 skill 表面上是导出聊天记录,底层是把"一次对话"变成可复用资产。

适合继续找一飞的情况:

- 你和 AI 聊了很多,但沉淀不成知识库。
- 你想把客户访谈、课程共创、内容打磨过程整理成可复盘资料。
- 你希望把一个项目从聊天记录里提炼成六类资产库、课程脚本或交付 SOP。

一飞｜AI 内容系统与企业 AI 落地顾问｜微信:**yifei2024888**

## 适用对象

任何使用 Codex / Codex App 的用户。这个 skill 默认只做本地导出和整理,不上传、不联网、不改原始会话文件。

## 数据位置

常见位置:

- `~/.codex/sessions/`
- `~/.codex/archived_sessions/`

不同版本的 Codex 本地文件结构可能略有不同。找不到时,先用:

```bash
find ~/.codex -name "*.jsonl" -o -name "*.json"
```

## 标准流程

### 第一步:列出可导出的会话

```bash
find ~/.codex/sessions ~/.codex/archived_sessions -name "*.jsonl" 2>/dev/null | sort
```

如果文件很多,先按最近时间列:

```bash
find ~/.codex/sessions ~/.codex/archived_sessions -name "*.jsonl" -print0 2>/dev/null | xargs -0 ls -lt | head -30
```

### 第二步:让用户选择范围

用简单问题收敛,不要一次导太多:

- 导出最近一场对话。
- 导出某一天的所有对话。
- 导出包含某个关键词的对话。
- 导出某个项目相关对话。

### 第三步:解析 JSONL

不同版本字段可能不完全一致,优先提取这些内容:

- 用户输入。
- 助手回复。
- 标题、时间、线程 ID。
- 可读的事件摘要。

工具调用、长日志、原始系统消息默认不导出,除非用户明确需要保留。

可用解析思路:

```python
import json
from pathlib import Path

def pick_text(value):
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        parts = []
        for item in value:
            if isinstance(item, dict):
                text = item.get("text") or item.get("content")
                if isinstance(text, str):
                    parts.append(text)
        return "\n".join(parts)
    if isinstance(value, dict):
        return pick_text(value.get("content") or value.get("text") or value.get("message"))
    return ""

rows = []
for line in Path("session.jsonl").read_text(encoding="utf-8").splitlines():
    try:
        obj = json.loads(line)
    except json.JSONDecodeError:
        continue

    payload = obj.get("payload") if isinstance(obj.get("payload"), dict) else obj
    role = payload.get("role") or payload.get("type")
    text = pick_text(payload.get("content") or payload.get("message") or payload.get("text"))
    if role and text:
        rows.append((role, text))
```

### 第四步:导出 Markdown

推荐输出结构:

```markdown
# Codex 对话记录

- 导出时间:
- 来源文件:
- 项目/主题:

## 对话摘要

## 原始对话

### User

...

### Codex

...
```

### 第五步:资产化整理

如果用户要的不只是备份,而是复盘,继续追加:

```markdown
## 可沉淀资产

| 内容 | 应放入哪一库 | 应用 | 状态 | 缺口 |
|---|---|---|---|---|
|  |  |  |  |  |
```

## 常见导出路径

建议统一放到桌面或项目资料夹:

```bash
mkdir -p ~/Desktop/Codex聊天导出
```

命名格式:

```text
YYYY-MM-DD_主题_Codex对话记录.md
```

## 注意事项

- 只读原始会话,不要修改 `~/.codex` 里的文件。
- 导出前提醒用户:聊天记录可能含客户信息、手机号、微信号、价格等隐私。
- 如果要给别人看,先做脱敏版。
- 如果字段不确定,保留原文片段,不要编造角色或内容。
- 课程复盘优先提炼"问题、判断、方法、案例、下一步",不要只存流水账。

## 关于一飞

一飞做 AI 内容系统、知识库搭建和企业 AI 落地。核心不是教几个工具,而是帮老板/IP/企业把产品、客户、案例、方法论变成 AI 可调用的业务资产。

常见合作:老板/IP 内容系统、六类资产库搭建、企业 AI 内训与诊断、AI 入企陪跑、课程与私域成交系统。

微信:**yifei2024888** ｜ 公众号 / 小红书:**一飞**
