---
title: FDE → OPC 一年自学大纲
aliases:
  - FDE一年学习计划
  - OPC能力准备路线
tags:
  - FDE
  - OPC
  - AI应用工程
  - 企业AI
  - 学习计划
status: active
created: 2026-07-17
updated: 2026-07-17
duration: 52周
study_mode: 独立自学
---

# FDE → OPC 一年自学大纲

> 版本：2026-07-17  
> 适用对象：零 Python 基础、AI 工具初级使用者、每天可投入约 8 小时，希望一年后具备 FDE（Forward Deployed Engineer，前线部署工程师）能力底座，并为未来 OPC（One Person Company，一人公司）做准备。

---

## 1. 这套大纲的目标与边界

### 一年后的目标

能够独立完成以下闭环：

1. 研究一个陌生行业；
2. 拆解企业业务流程；
3. 判断哪些问题适合 AI、普通自动化或暂时不做；
4. 设计数据、模型、工具、人工审批和风险边界；
5. 在 AI 辅助下开发一个可运行的中小型系统；
6. 建立测试集、评估指标、日志、权限和故障处理；
7. 输出需求说明、解决方案、试点方案、验收方案和复盘；
8. 形成个人 FDE 作品集，为后续选择 OPC 垂直行业做准备。

### 不把以下内容设为学习前提

- 当前公司必须有客户；
- 必须参与某个真实项目；
- 必须得到同事或技术人员指导；
- 必须找到真实用户测试；
- 必须在一年内创业或实现收入目标。

当前公司的业务可以由学习者自行用于实践验证，但不影响本大纲的学习进度和通关标准。

### 资料选择原则

1. **国外大学课程、技术官方文档优先**；
2. **官方英文原文优先于二手中文教程**；
3. 国外网站打不开或英文严重影响进度时，使用国内一线课程备用；
4. 一门主课负责建立体系，官方文档负责查证，个人项目负责掌握；
5. 不同时学习三套同类入门课；
6. 框架更新很快，涉及 OpenAI、FastAPI、Docker 等内容时，以官方文档当前版本为准。

---

## 2. 全年路线总览

| 阶段 | 周数 | 核心能力 | 阶段作品 |
|---|---:|---|---|
| 0. 环境与学习系统 | 第 1 周 | 命令行、编辑器、资料管理、AI 学习纪律 | 个人学习仓库 |
| 1. Python 与编程思维 | 第 2–9 周 | 变量、流程、函数、文件、异常、测试、面向对象 | 经营数据记录器 V0 |
| 2. Git、Shell 与工程习惯 | 第 10–13 周 | 版本控制、调试、项目结构、依赖和命令行 | 可维护的 Python 项目 |
| 3. SQL、数据库与 Web 基础 | 第 14–20 周 | 数据建模、SQL、HTTP、HTML 表单 | 经营管理系统 V1 |
| 4. FastAPI 与完整后端 | 第 21–28 周 | API、校验、认证、测试、PostgreSQL | 可登录的业务系统 V2 |
| 5. 大模型应用工程 | 第 29–36 周 | 结构化输出、评估、RAG、工具调用、工作流 | AI 经营助手 V3 |
| 6. 部署、安全与可靠性 | 第 37–42 周 | Docker、Linux、安全、日志、备份、恢复 | 在线系统 V4 |
| 7. FDE 业务与方案能力 | 第 43–48 周 | 行业研究、流程、场景、价值、范围、验收 | 三套模拟 FDE 案例 |
| 8. 毕业项目与 OPC 准备 | 第 49–52 周 | 综合分析、系统实现、方案表达、个人定位 | FDE 毕业项目与作品集 |

全年只维护一个主项目：**中小企业智能经营系统**。每一阶段在同一项目上升级，避免反复做互不相关的 Demo。

---

## 3. 每日与每周执行方式

### 每天 8 小时建议分配

| 模块 | 时间 | 要求 |
|---|---:|---|
| 主课或官方文档 | 2 小时 | 只学习当前阶段内容 |
| 主项目开发 | 3 小时 | 当天知识必须进入项目 |
| 测试与调试 | 1 小时 | 主动制造错误并修复 |
| FDE 业务案例 | 1 小时 | 每天拆解一个小流程或决策 |
| 技术英语 | 30 分钟 | 原文、翻译、术语、中文复述 |
| 知识库与复盘 | 30 分钟 | 记录概念、错误、决策和证据 |

### 每周六天循环

1. **周一：理解**——学习原理，画图，用中文复述；
2. **周二：复现**——跟随资料完成最小功能；
3. **周三：修改**——主动改变字段、输入或业务规则；
4. **周四：破坏**——制造错误输入、配置丢失、超时或连接失败；
5. **周五：重建**——不复制旧代码，重新实现核心部分；
6. **周六：考试**——写、改、修、讲各一次；
7. **周日：休息与轻复盘**——不增加新知识。

### 每项技术的掌握标准

```text
理解 → 复现 → 修改 → 破坏 → 修复 → 重建 → 讲解
```

仅仅“看懂”和“跟着做出来”不算掌握。

---

## 4. 阶段 0：环境与学习系统（第 1 周）

### 学习目标

- 理解文件、目录、终端、程序和进程；
- 安装 Python、VS Code、Git；
- 建立个人代码仓库和学习记录结构；
- 学会用 Codex 辅助解释、测试和审查，而不是替自己完成全部代码。

### 国外主资料

1. [MIT Missing Semester 2026](https://missing.csail.mit.edu/2026/)  
   只学习：Shell、开发环境、调试、Git、代码质量。
2. [MDN：Setting up your environment](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Environment_setup)
3. [Visual Studio Code: Getting Started](https://code.visualstudio.com/docs/getstarted/getting-started)

### 中文备用

1. [MDN Web 开发入门（中文）](https://developer.mozilla.org/zh-CN/docs/Learn_web_development/Getting_started)
2. MIT Missing Semester 页面使用浏览器翻译；中文视频只用于解释，不替代练习。

### 本周任务

- 新建 `fde-opc-learning` Git 仓库；
- 创建 `notes/`、`projects/`、`errors/`、`cases/`、`evaluations/`；
- 运行第一个 Python 程序；
- 完成 20 个基础终端命令练习；
- 写下《AI 辅助编程六条纪律》。

### 通关标准

- 能在终端切换目录、创建文件、运行 Python；
- 能解释工作目录、文件路径和环境变量；
- 能创建 Git 仓库并提交第一个版本。

---

## 5. 阶段 1：Python 与编程思维（第 2–9 周）

### 国外主课

1. [Harvard CS50P: Introduction to Programming with Python](https://cs50.harvard.edu/python/)  
2. [CS50P 的 edX 备用入口](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python)
3. [Python 官方教程（英文）](https://docs.python.org/3/tutorial/)

> 如果 CS50P 或 edX 无法访问，不要等待，直接使用下面的国内主课。Python 官方教程更适合作为查询手册，不适合作为零基础唯一主课。

### 国内一线备用主课

1. [北京理工大学《Python 语言程序设计》—中国大学 MOOC](https://www.icourse163.org/course/BIT-268001)
2. [Python123 练习平台](https://python123.io/)
3. [Python 官方中文教程](https://docs.python.org/zh-cn/3/tutorial/)
4. 可选教材：《Python 语言程序设计基础（第 3 版）》，嵩天、黄天羽、杨雅婷，高等教育出版社。

### 周度安排

| 周数 | 主题 | 必须完成的项目功能 |
|---|---|---|
| 2 | 变量、字符串、数字、输入输出 | 收入、成本、利润计算器 |
| 3 | 条件、循环、列表、字典 | 30 天经营数据统计 |
| 4 | 函数、参数、返回值、作用域 | 把计算逻辑拆成函数 |
| 5 | 文件、CSV、JSON | 保存和读取经营数据 |
| 6 | 异常处理、日志、第三方库 | 错误输入处理与错误日志 |
| 7 | 单元测试、pytest | 为核心计算函数写测试 |
| 8 | 类、对象、模块、类型标注 | 重构企业、门店、任务模块 |
| 9 | 综合重建 | 经营数据记录器 V0 |

### 测试资料

- [pytest: Get Started](https://docs.pytest.org/en/stable/getting-started.html)
- [Python `unittest` 官方文档](https://docs.python.org/3/library/unittest.html)

### 第 9 周考试

一天内从空目录完成：

- 录入收入和成本；
- 计算利润和利润率；
- 保存 JSON；
- 读取历史数据；
- 识别异常日期；
- 处理错误输入；
- 至少 10 个自动测试；
- Git 提交记录和 README。

---

## 6. 阶段 2：Git、Shell 与工程习惯（第 10–13 周）

### 国外主资料

1. [Pro Git 官方电子书](https://git-scm.com/book/en/v2)
2. [GitHub Skills](https://skills.github.com/)
3. [Introduction to GitHub 实操课程](https://github.com/skills/introduction-to-github)
4. [MIT Missing Semester：Git](https://missing.csail.mit.edu/2026/version-control/)
5. [MIT Missing Semester：Debugging and Profiling](https://missing.csail.mit.edu/2026/debugging-profiling/)

### 中文备用

1. [Pro Git 官方简体中文版](https://git-scm.com/book/zh/v2)
2. [GitHub 官方中文文档](https://docs.github.com/zh)

### 必学清单

- `init`、`status`、`add`、`commit`、`log`、`diff`；
- 分支、合并和冲突；
- `.gitignore`；
- 虚拟环境和依赖文件；
- 配置与环境变量；
- 日志和调试器；
- README、变更记录、架构决策记录（ADR）。

### 阶段任务

- 把 V0 重构成标准项目结构；
- 使用分支开发三个功能；
- 人为制造一次合并冲突并解决；
- 写三份 ADR：数据库选择、目录结构、错误处理策略；
- 从 Git 历史恢复一次错误修改。

---

## 7. 阶段 3：SQL、数据库与 Web 基础（第 14–20 周）

### SQL 国外主资料

1. [Harvard CS50 SQL](https://cs50.harvard.edu/sql/)
2. [SQLBolt 互动练习](https://sqlbolt.com/)
3. [PostgreSQL 官方教程](https://www.postgresql.org/docs/current/tutorial.html)
4. [PostgreSQL SQL Language Tutorial](https://www.postgresql.org/docs/current/tutorial-sql.html)

### SQL 中文备用

- 可选教材：《SQL 必知必会》；
- PostgreSQL 官方页面使用浏览器翻译；
- 前期练习使用 SQLite，理解关系数据库后再切换 PostgreSQL。

### Web 国外主资料

1. [MDN: Learn Web Development](https://developer.mozilla.org/en-US/docs/Learn_web_development)
2. [MDN: How the Web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)
3. [MDN: Your first website](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website)

### Web 中文备用

1. [MDN Web 开发学习区（中文）](https://developer.mozilla.org/zh-CN/docs/Learn_web_development)
2. [MDN Web 入门（中文）](https://developer.mozilla.org/zh-CN/docs/Learn_web_development/Getting_started/Your_first_website)

### 周度安排

| 周数 | 内容 | 产出 |
|---|---|---|
| 14 | SQL 查询、筛选、排序、聚合 | 20 条经营分析 SQL |
| 15 | 表、主键、外键、连接 | 企业经营数据模型 |
| 16 | 约束、事务、索引、规范化 | 数据库设计说明 |
| 17 | HTTP、URL、请求、响应、状态码 | HTTP 知识图 |
| 18 | HTML、表单、基础 CSS | 数据录入页面 |
| 19 | 浏览器调用 API、JSON | 页面与模拟 API 通信 |
| 20 | 综合项目 | 经营管理系统 V1 |

### 第 20 周考试

- 独立设计不少于 6 张表；
- 写出增删改查、连接和聚合查询；
- 解释浏览器、服务器、API、数据库的数据流；
- 完成一个可录入和查询数据的简单页面。

---

## 8. 阶段 4：FastAPI 与完整后端（第 21–28 周）

### 国外主资料

1. [FastAPI 官方教程](https://fastapi.tiangolo.com/tutorial/)
2. [Pydantic 官方文档](https://docs.pydantic.dev/latest/)
3. [HTTPX 官方文档](https://www.python-httpx.org/)
4. [pytest 官方文档](https://docs.pytest.org/en/stable/)

### 中文备用

1. [FastAPI 官方中文学习区](https://fastapi.tiangolo.com/zh/learn/)
2. [FastAPI 第一步（中文）](https://fastapi.tiangolo.com/zh/tutorial/first-steps/)

### 学习顺序

1. 路径参数、查询参数、请求体；
2. Pydantic 模型和数据校验；
3. 响应模型、状态码和错误处理；
4. 依赖注入；
5. 数据库访问和迁移；
6. 文件上传；
7. 用户认证与角色权限；
8. API 单元测试和集成测试。

### 周度安排

| 周数 | 内容 | 项目功能 |
|---|---|---|
| 21 | FastAPI 基础 | 企业、门店 API |
| 22 | Pydantic 与错误处理 | 严格的数据校验 |
| 23 | 数据库访问 | 收入、成本、任务接口 |
| 24 | PostgreSQL 与迁移 | 从 SQLite 迁移 |
| 25 | 登录与认证 | 用户登录 |
| 26 | 角色和数据权限 | 管理员、普通用户 |
| 27 | 测试与重构 | API 测试套件 |
| 28 | 综合考试 | 经营管理系统 V2 |

### 第 28 周考试

- 至少 10 个业务 API；
- PostgreSQL 数据库；
- 用户登录和两种权限；
- 统一错误响应；
- 至少 30 个自动测试；
- OpenAPI 接口文档；
- 完整 README。

---

## 9. 阶段 5：大模型应用工程（第 29–36 周）

### 国外主资料：先学系统，再学 Agent

1. [OpenAI Developer Quickstart](https://platform.openai.com/docs/quickstart/make-your-first-api-request)
2. [OpenAI Text Generation Guide](https://platform.openai.com/docs/guides/text)
3. [OpenAI Prompting Guide](https://platform.openai.com/docs/guides/prompting)
4. [OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
5. [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
6. [OpenAI Retrieval](https://platform.openai.com/docs/guides/retrieval)
7. [OpenAI File Search](https://platform.openai.com/docs/guides/tools-file-search)
8. [OpenAI Evals](https://platform.openai.com/docs/guides/evals)
9. [OpenAI Cookbook](https://cookbook.openai.com/)

### 国外课程补充

1. [DeepLearning.AI：ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
2. [DeepLearning.AI：Building Systems with the ChatGPT API](https://www.deeplearning.ai/courses/chatgpt-building-system)
3. [Anthropic：Building Effective AI Agents](https://resources.anthropic.com/building-effective-ai-agents)

> DeepLearning.AI 课程帮助形成直觉，OpenAI 官方文档负责当前 API 实现。旧课程代码如果与当前接口不同，以官方文档为准。

### 中文备用

- OpenAI、Anthropic 和 DeepLearning.AI 页面使用浏览器翻译；
- 先阅读英文标题、代码、参数名称，再查看中文翻译；
- 建立自己的中英术语表，不使用来源不明的“Prompt 大全”作为主资料。

### 周度安排

| 周数 | 内容 | 项目功能 |
|---|---|---|
| 29 | 模型 API、Token、上下文、成本 | AI 经营日报 |
| 30 | 结构化输出、校验、重试 | 固定 JSON 分析结果 |
| 31 | 测试集、错误分类、Evals | 100 条经营评估集 |
| 32 | Embedding、检索、引用、拒答 | 企业制度知识库 |
| 33 | 检索评估、文档更新 | 50 条 RAG 测试集 |
| 34 | Function Calling | 查询数据、查询制度 |
| 35 | 固定工作流、状态、审批 | 异常处理工作流 |
| 36 | Agent 边界与综合考试 | AI 经营助手 V3 |

### 第 36 周考试

- 100 条结构化输出评估；
- 50 条知识库评估；
- 至少 3 个工具；
- 重要操作必须有确认步骤；
- 记录调用成本、延迟和错误；
- 能解释为什么某些步骤用普通代码、某些用模型、某些才适合 Agent。

---

## 10. 阶段 6：部署、安全与可靠性（第 37–42 周）

### 国外主资料

1. [Docker Get Started](https://docs.docker.com/get-started/)
2. [Docker Introduction](https://docs.docker.com/get-started/introduction/)
3. [MIT Missing Semester 2026](https://missing.csail.mit.edu/2026/)
4. [OWASP Top 10](https://owasp.org/www-project-top-ten/)
5. [Google SRE 资源中心](https://sre.google/resources/)
6. [Google SRE：Testing for Reliability](https://sre.google/sre-book/testing-reliability/)
7. [Google SRE：Release Engineering](https://sre.google/sre-book/release-engineering/)
8. [Microsoft Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/)
9. [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)

### 中文备用

- [Docker 中文文档入口](https://docs.docker.com/)
- [OWASP Top 10 中文历史版本入口](https://owasp.org/www-project-top-ten/)
- 云平台部分只选择一个平台实际部署，不同时学习多个云平台。

### 周度安排

| 周数 | 内容 | 产出 |
|---|---|---|
| 37 | Linux、进程、端口、环境变量 | 部署操作笔记 |
| 38 | Docker、镜像、容器、数据卷 | Dockerfile |
| 39 | Docker Compose、数据库、网络 | 完整本地容器环境 |
| 40 | 密钥、认证、越权、注入、脱敏 | 安全检查表 |
| 41 | 日志、监控、备份、恢复、回滚 | 故障演练报告 |
| 42 | 综合部署 | 在线系统 V4 |

### 故障考试

主动模拟：

- 模型服务超时；
- 数据库断开；
- 环境变量缺失；
- 重复提交；
- 普通用户越权；
- 提示词注入；
- 数据误删；
- 新版本发布失败。

每次必须写：现象、原因、定位过程、修复、预防和验证。

---

## 11. 阶段 7：FDE 业务与方案能力（第 43–48 周）

### 国外主资料

1. [Stanford d.school：Design Thinking Bootleg](https://dschool.stanford.edu/tools/design-thinking-bootleg)
2. [Strategyzer：Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas)
3. 《The Mom Test》— Rob Fitzpatrick
4. 《User Story Mapping》— Jeff Patton
5. 《Thinking in Systems》— Donella H. Meadows
6. 《Value Proposition Design》— Alexander Osterwalder 等
7. 《The Pyramid Principle》— Barbara Minto

### 中文备用书目

1. 《妈妈测试》；
2. 《用户故事地图》；
3. 《系统之美》；
4. 《价值主张设计》；
5. 《金字塔原理》。

> 书名翻译和不同版本可能有差异。关键概念、图表和术语尽量对照英文原书或作者官方模板。

### 六周训练

| 周数 | 核心训练 | 必须输出 |
|---|---|---|
| 43 | 行业结构与商业模式 | 客户、收入、成本、角色、系统图 |
| 44 | 业务流程拆解 | 输入、角色、动作、判断、输出、指标、风险 |
| 45 | 问题诊断与场景评分 | AI、普通自动化、不做三类场景 |
| 46 | 价值、数据和风险 | 基线、收益假设、数据清单、风险清单 |
| 47 | 方案架构与范围 | 原流程、目标流程、架构、边界、审批 |
| 48 | 试点、验收和表达 | 试点方案、测试方案、验收表、20 分钟陈述 |

### 三个独立模拟案例

1. 宾馆经营；
2. 网吧或酒吧经营；
3. 纸厂或中小制造业。

每个案例必须包含：

- 行业地图；
- 三条核心流程；
- 问题清单；
- AI 场景评分；
- 数据和系统清单；
- 解决方案；
- 风险与权限；
- 评估与验收；
- 明确不做的内容。

---

## 12. 阶段 8：毕业项目与 OPC 准备（第 49–52 周）

### 第 49 周：陌生行业研究

- 选择过去没有经营过的行业；
- 优先使用年报、招股书、政府文件、行业协会和产品官方文档；
- 输出行业地图、角色、流程、系统和关键指标。

### 第 50 周：诊断与方案

- 问题优先级；
- AI 适配度；
- 原流程和目标流程；
- 数据流和架构；
- 价值假设；
- 风险和边界；
- 两周试点方案。

### 第 51 周：原型、测试与交付包

完成：

1. 可运行原型；
2. 需求说明；
3. 架构图；
4. 测试集；
5. AI 评估；
6. 安全检查；
7. 使用手册；
8. 验收方案；
9. 故障与复盘报告。

### 第 52 周：个人能力审计与 OPC 方向

回答：

- 自己最强的行业认知是什么；
- 哪类问题最适合标准化；
- 哪些系统一个人能够长期维护；
- 哪些服务可以远程交付；
- 哪些环节适合 AI 自动化；
- 哪些工作必须由自己负责；
- 哪些高风险项目不适合 OPC；
- 下一年需要通过什么真实实践验证。

---

## 13. 个人资料库结构

```text
FDE-OPC-Learning/
├── 00-年度计划/
├── 01-技术概念/
├── 02-代码项目/
├── 03-错误与故障/
├── 04-AI评估集/
├── 05-FDE案例/
├── 06-架构决策/
├── 07-技术英语/
├── 08-月度考试/
└── 09-个人作品集/
```

### 每条技术笔记必须回答

1. 它是什么；
2. 它解决什么问题；
3. 什么时候使用；
4. 什么时候不使用；
5. 在主项目中如何实现；
6. 最容易在哪里出错；
7. 如何测试。

---

## 14. AI 辅助编程纪律

1. AI 一次只实现一个清晰功能；
2. 修改前先说明涉及哪些文件和风险；
3. 修改后必须查看差异；
4. 关键业务逻辑必须有测试；
5. 自己必须能用中文解释数据流；
6. 每周至少一次不用 AI 的闭卷练习；
7. 不允许 AI 代做阶段考试；
8. AI 的技术结论必须用运行结果或官方文档验证；
9. 项目失败时先阅读日志，再向 AI 提问；
10. 不把“代码运行了”误认为“系统可靠”。

---

## 15. 月度检查表

每四周检查一次：

| 指标 | 最低要求 |
|---|---:|
| 可运行的新功能 | 4 个 |
| 自己编写或审查的自动测试 | 12 个 |
| 完整错误复盘 | 8 个 |
| 业务流程拆解 | 4 个 |
| 架构决策记录 | 2 个 |
| 录屏讲解 | 1 次 |
| 闭卷重建 | 1 次 |

阶段是否通过，以作品和考试为准，不以“视频是否看完”为准。

---

## 16. 第一个月的资料只保留这些

### 国外入口可访问时

1. [CS50P](https://cs50.harvard.edu/python/)
2. [Python 官方教程](https://docs.python.org/3/tutorial/)
3. [Pro Git](https://git-scm.com/book/en/v2)
4. [pytest Get Started](https://docs.pytest.org/en/stable/getting-started.html)

### 国外入口打不开时

1. [北京理工大学《Python 语言程序设计》](https://www.icourse163.org/course/BIT-268001)
2. [Python123](https://python123.io/)
3. [Python 官方中文教程](https://docs.python.org/zh-cn/3/tutorial/)
4. [Pro Git 官方简体中文版](https://git-scm.com/book/zh/v2)

### 第一个月禁止增加

- LangChain；
- 多 Agent；
- 模型微调；
- React；
- Kubernetes；
- 多种数据库；
- 第二门编程语言；
- 与当前阶段无关的高价课程。

---

## 17. 年度毕业评分

| 能力 | 分值 |
|---|---:|
| 软件工程基础 | 20 |
| AI 应用工程 | 20 |
| 测试、安全与可靠性 | 15 |
| 业务诊断 | 15 |
| 方案与架构设计 | 15 |
| 项目范围、评估与验收 | 10 |
| 文档和表达 | 5 |

毕业要求：

- 总分不低于 75；
- 任一大项不能低于该项满分的 60%；
- 毕业系统可以运行；
- 关键功能有自动测试；
- AI 功能有独立评估集；
- 关键结论有证据或明确标注为假设；
- 能在不看稿的情况下讲清业务、架构、风险和验收方法。

---

## 18. 最后提醒

这份大纲的核心不是收集链接，而是持续形成能力证据：

```text
学习一项知识
→ 做进同一个项目
→ 主动制造问题
→ 修复并测试
→ 写下决策依据
→ 独立重新实现
→ 用业务语言讲清楚
```

国外主资料是第一选择，但“打不开”不能成为停学理由。出现访问障碍时立刻切换到列出的中文一线备用资料；掌握概念后，再通过官方英文文档校对术语和接口。
