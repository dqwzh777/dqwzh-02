# 海外 AI 软件课前安装手册（Windows 与 Mac）

> 适用场景：企业 AI 通识课、AI 办公课、AI 编程课的课前准备  
> 核对日期：2026 年 7 月 10 日  
> 原则：只从官方网站或系统应用商店下载；产品要求会变化，每次开课前应复核文末官方链接。

## 一、先看结论：学员到底要装什么

### A 组：所有学员必须准备

1. 一台能正常使用的 Windows 或 Mac 电脑。
2. 最新版 Chrome 浏览器；Edge、Safari 可作为备用。
3. 一个能正常收邮件、收验证码的个人邮箱。
4. 根据课程安排提前注册 ChatGPT、Claude、Google、Perplexity 等账号。
5. 经单位允许、符合所在地法律法规和服务商条款的网络环境。
6. 至少保留 10 GB 可用磁盘空间，并把系统时间设为自动同步。
7. 公司电脑需要提前确认：能否安装软件、能否打开 Microsoft Store、是否需要 IT 管理员密码。

### B 组：AI 通识或办公课建议安装

| 软件 | 是否必须下载 | 推荐使用方式 | 账号准备 |
|---|---|---|---|
| ChatGPT | 建议；装不了可用网页 | 桌面端 + 网页备用 | OpenAI/ChatGPT 账号 |
| Claude | 建议；装不了可用网页 | 桌面端 + 网页备用 | Claude 账号 |
| Gemini | 不必下载 | 浏览器打开网页 | Google 账号 |
| NotebookLM | 不必下载 | 浏览器打开网页 | Google 账号，工作/学校账号可能需管理员开启 |
| Perplexity | 不必下载 | 浏览器打开网页 | 建议提前注册；部分高级功能需订阅 |

### C 组：AI 编程课额外安装

建议按以下顺序安装，后装的软件会用到前面的环境：

1. Git
2. VS Code
3. Python 3
4. Node.js LTS
5. Cursor（课程使用时）
6. Codex 或 Claude Code（课程使用时）
7. WSL2（仅 Windows 进阶课程需要，不再是默认必装项）

> 重要：ChatGPT、Claude、Gemini、NotebookLM、Perplexity 的普通聊天功能都不要求先安装 Python、Node.js、Git 或浏览器插件。不要让普通办公课学员安装无关开发环境。

## 二、网络、地区与账号准备

### 1. 关于学员常说的“魔法上网”

海外 AI 服务通常需要稳定访问其官网、登录验证页、模型接口和软件下载地址。某些国家或地区可能无法直接访问，或者并不在服务商官方支持范围内。

培训组织方应这样处理：

1. 先确认学员所在地是否在各服务商的官方支持地区。
2. 由企业 IT 提供合法合规的国际网络、企业代理或允许的访问方案。
3. 开课前实际测试官网、登录、验证码、上传文件和模型回复，不要只测试“网页能打开”。
4. 不在培训群传播来源不明的代理软件、共享节点、破解客户端或绕过地区限制的方法。
5. 网络能连通不等于账号符合服务条款。账号注册地、实际使用地、手机号和付款地区应真实、一致、受官方支持。

特别提醒：OpenAI 明确说明，从其未支持的国家或地区访问或提供访问，可能导致账号被阻止或暂停。Claude、Gemini、NotebookLM 等也有各自的支持地区要求。因此，“装一个网络工具就一定能用”是不准确的，也可能带来账号和合规风险。

### 2. 开课前网络验收

让每位学员分别打开下列课程会使用的网站，并完成一次真实操作：

| 用途 | 官方地址 | 验收动作 |
|---|---|---|
| ChatGPT | https://chatgpt.com/ | 登录并发送“你好” |
| Claude | https://claude.ai/ | 登录并发送“你好” |
| Gemini | https://gemini.google.com/ | 登录并完成一次问答 |
| NotebookLM | https://notebooklm.google.com/ | 登录并进入首页 |
| Perplexity | https://www.perplexity.ai/ | 完成一次搜索 |
| GitHub | https://github.com/ | 编程课学员登录并打开个人主页 |

如果使用公司代理或防火墙，还要确认：

- 登录后的跳转页面不会被拦截。
- WebSocket 或流式回答不会中途断开。
- 可以下载 `.exe`、`.msi`、`.dmg`、`.pkg` 等官方安装文件。
- 可以访问软件更新服务器。
- 公司安全软件不会隔离安装包或命令行工具。

### 3. 账号与验证准备

- 每位学员使用自己的账号，不多人共用个人账号。
- 提前完成邮箱验证、手机验证和双重验证；上课时要能打开邮箱或验证器。
- Google Workspace、学校账号和企业账号可能需要管理员开启 Gemini、NotebookLM 等服务。
- Codex、Claude Code、GitHub Copilot 等功能可能需要对应付费计划、企业席位或 API 计费账号。讲师应在采购后逐个分配权限。
- 不建议现场临时注册几十个相似账号，容易触发风控。
- 不承诺某一银行卡、手机号或付款方式必然可用；付款地区和账户资料应符合平台要求。

## 三、电脑统一前置检查

### Windows 推荐基线

- 推荐 Windows 11 64 位，并完成系统更新。
- Windows 10 应至少为较新的 64 位版本；具体软件要求见后文。
- 建议 8 GB 以上内存，AI 编程课推荐 16 GB。
- 至少 10 GB 可用空间，编程课建议 20 GB。
- 能使用管理员权限，或已由 IT 批准安装。
- Microsoft Store 和 Windows Package Manager（`winget`）可用。

查看方法：打开“设置 → 系统 → 系统信息/关于”，记录 Windows 版本、系统类型和处理器架构。

### Mac 推荐基线

- 为兼容 ChatGPT 桌面端，统一推荐 macOS 14 或更高版本。
- ChatGPT Mac 桌面端只支持 Apple 芯片 M1 或更新型号，不支持 Intel Mac。
- 建议 8 GB 以上内存，AI 编程课推荐 16 GB。
- 至少 10 GB 可用空间，编程课建议 20 GB。
- 学员知道本机登录密码，安装时可能需要授权。

查看方法：点击左上角苹果菜单 →“关于本机”，记录 macOS 版本，以及“芯片”是 Apple M 系列还是 Intel。

### 通用基础设置

1. 将系统日期、时间和时区设为自动。
2. 更新 Chrome、Edge 或 Safari。
3. 关闭会拦截所有下载的临时浏览器设置；公司管控设备交由 IT 调整。
4. 不要关闭系统防病毒或防火墙来换取安装成功，应让 IT 对官方软件做合规放行。
5. 删除来源不明的同名安装包，只保留从官方地址重新下载的版本。

## 四、Windows 安装手册

### 第一步：安装 Chrome

1. 用 Edge 打开 https://www.google.com/chrome/ 。
2. 下载 Windows 版本。
3. 双击安装文件，等待自动安装。
4. 打开 Chrome，登录不是必须的；能正常访问课程网站即可。
5. 不要预装所谓“ChatGPT 增强”“Claude 中文版”等来历不明的扩展。

### 第二步：安装 ChatGPT

前置条件：Windows 10 版本 17763.0 或更高，支持 x64 和 ARM64；Microsoft Store 未被公司策略禁用。

1. 打开 https://openai.com/chatgpt/desktop/ 。
2. 选择 Windows 下载，跳转 Microsoft Store。
3. 点击“获取/安装”。
4. 安装后从开始菜单打开 ChatGPT。
5. 登录自己的 ChatGPT 账号并发送一条测试消息。
6. 若 Store 被禁用或安装失败，直接使用 https://chatgpt.com/ 网页版，不影响普通 AI 课程。

### 第三步：安装 Claude Desktop

前置条件：Windows 10 或更高；Claude 账号；所在地属于 Anthropic 支持范围。

1. 打开 https://claude.ai/download 。
2. 选择 Windows 版本。
3. 打开下载的安装程序并按提示安装。
4. 从开始菜单启动 Claude。
5. 登录并完成一次问答。

### 第四步：准备网页型 AI 工具

以下软件在 Windows 电脑上不要求安装客户端，建议在 Chrome 收藏夹建立“AI 课堂”文件夹：

- Gemini：https://gemini.google.com/
- NotebookLM：https://notebooklm.google.com/
- Perplexity：https://www.perplexity.ai/

分别登录并测试。Gemini 需要受支持的 Google 账号和浏览器；NotebookLM 的工作或学校账号可能需要管理员开启。

### 第五步：AI 编程课安装 Git

1. 打开 https://git-scm.com/install/windows 。
2. 按处理器选择 x64 或 ARM64 安装包；多数 Windows 电脑为 x64。
3. 双击安装，初学者保持默认选项即可。
4. 安装完成后重新打开终端。
5. 在 PowerShell 输入 `git --version`，能显示版本号即通过。

Git for Windows 还会提供 Git Bash。Claude Code 在 Windows 原生模式下不强制要求 Git Bash，但安装 Git 后兼容性和项目管理体验更好。

### 第六步：安装 VS Code

1. 打开 https://code.visualstudio.com/Download 。
2. 下载 Windows 64 位安装程序。
3. 安装时建议勾选“添加到 PATH”和“使用 Code 打开”。
4. 启动 VS Code。
5. 只安装课程明确要求的扩展。常用选装项：Chinese Language Pack、Python、GitHub Copilot。

GitHub Copilot 不是 VS Code 自带免费功能。使用前需要 GitHub 账号，以及试用、个人订阅、教育资格或企业分配的席位。

### 第七步：安装 Python 3

1. 打开 https://www.python.org/downloads/windows/ 。
2. 下载官方 64 位安装程序。
3. 安装首页勾选“Add Python to PATH”。
4. 完成安装后重新打开 PowerShell。
5. 输入 `python --version`；若无结果，再试 `py --version`。

普通聊天课不需要 Python。只有自动化、数据处理、API 或 AI 编程课程才安装。

### 第八步：安装 Node.js LTS

1. 打开 https://nodejs.org/en/download 。
2. 选择 LTS 版本，不选 Current 测试新版本。
3. 下载与电脑架构一致的 Windows 安装包并保持默认安装。
4. 重新打开 PowerShell。
5. 输入 `node --version` 和 `npm --version`，均能显示版本号即通过。

### 第九步：安装 Cursor（课程使用时）

前置条件：Windows 10/11；确认电脑是 x64 还是 ARM64；准备 Cursor 账号。

1. 打开 https://www.cursor.com/downloads 。
2. 选择 Windows 10/11 的 x64 或 ARM64 版本。
3. 安装并启动 Cursor。
4. 登录账号。
5. 首次启动可导入 VS Code 设置，但统一授课时建议使用讲师规定的干净配置。
6. 打开一个测试文件夹，确认聊天、代码补全和终端均可使用。

### 第十步：使用 Codex（课程使用时）

初学者优先使用 ChatGPT Windows 桌面端中的 Codex 工作流；Windows 11 是官方推荐基线，较新的 Windows 10 为尽力支持。Git、Node.js 和 Python 不是启动桌面端的硬性前置，但安装后更适合实际编程任务。

1. 安装 ChatGPT Windows 桌面端并登录支持 Codex 的 ChatGPT 账号。
2. 安装 Git；按课程项目再安装 Node.js、Python 或其他语言环境。
3. 在桌面端添加课程项目文件夹。
4. 首次使用保持“需要批准/Ask for approval”等受控权限，不要直接给全盘访问。
5. 企业电脑若要使用更强的 Windows 沙箱，可能需要管理员批准相关设置。

若课程明确讲 Codex CLI，可按官方页面 https://developers.openai.com/codex/cli 执行当时最新安装方式。CLI 安装命令容易变化，课前不要沿用旧截图或旧命令。

### 第十一步：安装 Claude Code（课程使用时）

前置条件：Windows 10 1809 或更高、4 GB 以上内存、x64/ARM64、网络可用；需要 Claude Pro、Max、Team、Enterprise 或 Console 账号，免费 Claude 计划不包含 Claude Code。

推荐图形方式：安装 Claude Desktop，在其中使用 Claude Code，适合不熟悉终端的学员。

命令行方式：

1. 建议先安装 Git for Windows。
2. 打开 PowerShell；无需以管理员身份运行。
3. 按官方安装页 https://code.claude.com/docs/en/setup 执行 Windows PowerShell 安装命令。
4. 安装完成后输入 `claude --version`。
5. 输入 `claude`，按浏览器提示完成登录。
6. 输入 `claude doctor` 完成环境检查。

Windows 现在可以原生运行 Claude Code。WSL2 只在课程使用 Linux 工具链、需要 Linux 沙箱或项目本来就在 WSL 中时安装。

### 第十二步：WSL2（仅进阶选装）

满足以下任一情况才安装：课程明确使用 Linux 命令、Docker/Linux 工具链，或 Codex/Claude Code 项目存放在 WSL 中。

1. 先征得公司 IT 同意；WSL 可能受 BIOS、虚拟化或企业策略影响。
2. 用管理员 PowerShell 按微软官方文档安装 WSL2。
3. 安装 Ubuntu 等发行版并完成用户名、密码设置。
4. 在 WSL 内单独安装 Git、语言环境和对应 CLI。
5. 不要把 Windows 版和 WSL 版 Node/Python 混着用。

## 五、Mac 安装手册

### 第一步：更新系统并确认芯片

1. 苹果菜单 →“关于本机”，确认 macOS 版本和芯片。
2. 苹果菜单 →“系统设置 → 通用 → 软件更新”，完成必要更新。
3. 若是 Intel Mac，ChatGPT Mac 桌面端不能安装，直接使用网页版。

### 第二步：安装 Chrome

1. 用 Safari 打开 https://www.google.com/chrome/ 。
2. 下载适合 Mac 的版本。
3. 打开 `.dmg`，把 Chrome 拖入“应用程序”。
4. 从“应用程序”启动 Chrome；若系统提示，确认打开官方签名应用。

### 第三步：安装 ChatGPT

前置条件：macOS 14 或更高，并且是 Apple Silicon M1 或更高型号。Intel Mac 不支持该桌面端。

1. 打开 https://openai.com/chatgpt/desktop/ 。
2. 下载 macOS 版本。
3. 打开下载的 `.dmg` 文件。
4. 将 ChatGPT 拖入“Applications/应用程序”。
5. 从“应用程序”启动并登录。
6. 若系统或芯片不支持，使用 https://chatgpt.com/ 网页版。

### 第四步：安装 Claude Desktop

前置条件：macOS 11 或更高；Claude 账号；所在地属于 Anthropic 支持范围。

1. 打开 https://claude.ai/download 。
2. 下载 macOS 版本。
3. 打开 `.dmg`，将 Claude 拖入“应用程序”。
4. 启动 Claude，按系统提示授予课程确实需要的权限。
5. 登录并完成一次问答。

### 第五步：准备网页型 AI 工具

在 Chrome 收藏以下地址并提前登录：

- Gemini：https://gemini.google.com/
- NotebookLM：https://notebooklm.google.com/
- Perplexity：https://www.perplexity.ai/

这些服务普通电脑课程不需要安装 Mac 客户端。Perplexity 的部分新本机代理能力可能只支持较新的 macOS，并涉及本地文件和应用权限；除非课程明确使用，否则不要作为统一必装项。

### 第六步：AI 编程课安装 Git

Mac 可通过 Apple Command Line Tools 或 Homebrew 安装 Git。面向初学者，最简单的验证方式是：

1. 打开“终端”。
2. 输入 `git --version`。
3. 如果系统提示安装 Command Line Tools，按提示完成。
4. 再次输入 `git --version`，显示版本号即通过。

需要统一版本管理时，可参考 https://git-scm.com/install/mac 使用 Homebrew 安装。普通学员不必同时安装多套 Git。

### 第七步：安装 VS Code

1. 打开 https://code.visualstudio.com/Download 。
2. 下载适合 Mac 的 Universal、Apple Silicon 或 Intel 版本。
3. 解压后把 Visual Studio Code 拖入“应用程序”。
4. 启动 VS Code。
5. 只安装课程要求的扩展，例如 Chinese Language Pack、Python、GitHub Copilot。

### 第八步：安装 Python 3

1. 打开 https://www.python.org/downloads/macos/ 。
2. 下载官方 macOS 安装包。
3. 打开 `.pkg` 并按提示安装。
4. 重新打开终端。
5. 输入 `python3 --version`，能显示版本号即通过。

不要依赖系统可能自带的旧 Python；课程统一使用 `python3`。

### 第九步：安装 Node.js LTS

1. 打开 https://nodejs.org/en/download 。
2. 选择 LTS 版本和对应芯片架构。
3. 下载 `.pkg` 并安装。
4. 重新打开终端。
5. 输入 `node --version` 和 `npm --version` 验收。

### 第十步：安装 Cursor（课程使用时）

1. 打开 https://www.cursor.com/downloads 。
2. Apple 芯片选择 Arm64；Intel Mac 选择 x64；不确定可选 Universal。
3. 打开安装文件，将 Cursor 拖入“应用程序”。
4. 启动并登录 Cursor 账号。
5. 打开课程测试文件夹，验证聊天、补全和终端。

### 第十一步：使用 Codex（课程使用时）

1. 安装 ChatGPT Mac 桌面端并登录支持 Codex 的 ChatGPT 账号。
2. 安装 Git；按课程项目安装 Node.js、Python 或其他语言环境。
3. 在桌面端添加课程项目文件夹。
4. 首次任务保持受控权限，逐次检查文件修改和命令执行。

若课程明确使用 Codex CLI，开课前从 https://developers.openai.com/codex/cli 核对最新安装方式，并在终端完成登录和测试。不要把 API Key 直接发在群里或写进课程项目文件。

### 第十二步：安装 Claude Code（课程使用时）

前置条件：macOS 13 或更高、4 GB 以上内存、x64/ARM64、网络可用；需要 Claude Pro、Max、Team、Enterprise 或 Console 账号。

推荐图形方式：安装 Claude Desktop，在桌面端进入 Claude Code。

命令行方式：

1. 打开“终端”。
2. 按 https://code.claude.com/docs/en/setup 的 macOS 原生安装说明操作。
3. 安装完成后输入 `claude --version`。
4. 输入 `claude`，在浏览器完成登录。
5. 输入 `claude doctor` 验证环境。

官方目前推荐原生安装；不应为了安装 Claude Code 而强制所有学员先装 Node.js。只有选择 npm 安装方式或课程项目本身需要 Node.js 时才安装 Node.js。

## 六、浏览器插件与编辑器插件

### 默认不统一安装的浏览器插件

普通 AI 课程只需浏览器，不需要任何“ChatGPT 插件”“Claude 插件”或第三方账号助手。第三方扩展可能读取网页内容、提示词、文件和登录信息。

只有课程明确演示某个扩展时，才应：

1. 由讲师给出官方商店链接和发布者名称。
2. 核对扩展要求的网页访问权限。
3. 不给扩展访问所有网站的权限，除非功能确实需要并得到企业批准。
4. 课程结束后按企业规定保留或卸载。

### AI 编程课可选的 VS Code 扩展

| 扩展 | 什么时候安装 | 额外条件 |
|---|---|---|
| Chinese Language Pack | 学员需要中文界面 | 无账号要求 |
| Python（Microsoft） | Python 课程 | 已安装 Python 3 |
| GitHub Copilot | 课程讲 Copilot | GitHub 账号 + 可用席位/订阅 |
| Dev Containers | 课程讲容器开发 | Docker 与企业 IT 许可 |

Cursor、Codex、Claude Code 本身不等于 VS Code 插件；课程应先决定主工具，不要让学员同时装多个功能重叠的 AI 编程助手。

## 七、使用前必须讲清楚的安全事项

1. 不把客户名单、身份证号、合同原件、未公开财务数据、源代码密钥等直接上传到个人 AI 账号。
2. 企业资料优先使用公司批准的 Business、Enterprise、Team 或受控 API 环境。
3. 不把 API Key、密码、验证码发到培训群、截图或代码仓库。
4. AI 编程工具首次使用时保持审批和沙箱限制；不要轻易选择全盘访问或跳过所有权限确认。
5. 让 AI 执行删除文件、批量改文件、安装软件、运行脚本前，先备份或提交 Git。
6. AI 输出可能出错，涉及法律、医疗、财务、对外发布和生产系统时必须人工复核。
7. 只下载官方签名软件，不使用“绿色版”“破解版”“汉化特别版”或网盘转存安装包。
8. 共享电脑使用完应退出账号，并清理下载文件和浏览器会话。

## 八、讲师课前 48 小时验收清单

### 所有课程

- [ ] 已确定主工具和备用工具，不在现场临时决定。
- [ ] 已核对学员所在地与各平台支持地区。
- [ ] 培训网络能完成登录、问答、上传和下载。
- [ ] 投屏电脑和至少一台学员电脑完成全流程测试。
- [ ] 每位学员有独立账号，能接收验证码。
- [ ] 公司电脑的安装权限、Store 权限和防火墙放行已确认。
- [ ] 已准备网页版备用方案和国内合规备用工具。
- [ ] 已告知学员不要上传真实敏感资料。

### AI 编程课

- [ ] `git --version` 通过。
- [ ] VS Code 或 Cursor 能打开课程项目。
- [ ] Python 课的 `python --version`、`py --version` 或 `python3 --version` 通过。
- [ ] Node 课的 `node --version` 和 `npm --version` 通过。
- [ ] Codex 或 Claude Code 已登录并完成一次测试任务。
- [ ] 付费计划、API 余额或企业席位已分配。
- [ ] 课程项目不含真实密钥和生产数据。
- [ ] Windows 学员已明确使用原生环境还是 WSL，避免现场混用。

### 单个学员通过标准

学员完成以下动作才算准备完成：

1. 能打开主工具并登录。
2. 能发送消息并收到完整回复。
3. 能打开课程备用工具。
4. 编程课能打开项目，并通过课程要求的版本检查。
5. 知道哪些资料不能上传，知道如何退出自己的账号。

## 九、可直接发给学员的课前通知

各位同事，本次培训会使用海外 AI 工具，请在开课前 48 小时完成以下准备：

1. 更新 Windows 或 macOS，并安装最新版 Chrome。
2. 准备一个能正常收验证码的个人邮箱。
3. 按课程通知注册并登录 ChatGPT、Claude、Google 或 Perplexity 账号。
4. 在培训地点实际打开课程网址，发送一条测试消息，确认能收到完整回复。
5. 公司电脑如果不能安装软件，请提前联系 IT；客户端装不了时可先用网页版。
6. AI 编程课学员还需安装 Git、VS Code、Python 3、Node.js LTS，以及课程指定的 Cursor、Codex 或 Claude Code。
7. 不要安装来源不明的“中文版”、破解版、共享账号工具或浏览器扩展。
8. 培训练习请使用脱敏材料，不要上传客户隐私、合同原件、密码、密钥或公司机密。

完成后请回复：电脑系统版本 + 主工具已登录 + 已完成一次测试问答。遇到问题请把错误页面截图发给助教，但截图前遮住邮箱、手机号、验证码和密钥。

## 十、常见问题处理

| 问题 | 常见原因 | 处理方式 |
|---|---|---|
| 官网打不开 | 网络、DNS、防火墙或地区不可用 | 先确认官方支持地区，再联系企业 IT；切换课程备用工具 |
| 能打开但不能登录 | 验证码、账号类型、地区或风控 | 使用本人账号，检查邮箱/验证器；不要反复批量注册 |
| Windows Store 不能安装 | 公司策略禁用 Store | 联系 IT 部署；普通课先用网页版 |
| Mac 提示应用不兼容 | macOS 太旧或 Intel 芯片 | 更新系统；ChatGPT Intel Mac 使用网页版 |
| 安装包被隔离 | 来源异常或安全策略 | 删除安装包，从官网重下；交 IT 核验签名和放行 |
| 网页回答到一半断开 | 网络代理、WebSocket 或会话问题 | 刷新并重新登录；让 IT 检查代理和长连接 |
| 终端提示命令不存在 | 安装未完成或 PATH 未刷新 | 关闭并重开终端；重新检查安装步骤 |
| 编程助手不能改文件 | 文件夹权限或沙箱限制 | 选择正确项目文件夹，按需授权，不直接开放全盘 |
| 免费账号功能不够 | 功能属于付费计划或企业席位 | 讲师提前采购并分配；不要等到课堂现场处理付款 |

## 十一、官方核对链接

### OpenAI

- ChatGPT 桌面端：https://openai.com/chatgpt/desktop/
- ChatGPT Windows 要求：https://help.openai.com/en/articles/9982051
- ChatGPT macOS 要求：https://help.openai.com/en/articles/9395554
- ChatGPT 支持地区：https://help.openai.com/en/articles/7947663-chatgpt-supported-countries
- Codex CLI：https://developers.openai.com/codex/cli
- Codex Windows：https://developers.openai.com/codex/windows

### Anthropic

- Claude Desktop 安装：https://support.anthropic.com/en/articles/10065433-installing-claude-for-desktop
- Claude 下载：https://claude.ai/download
- Claude Code 安装与要求：https://code.claude.com/docs/en/setup
- Anthropic 支持地区：https://www.anthropic.com/supported-countries

### Google 与 Perplexity

- Gemini 登录要求：https://support.google.com/gemini/answer/13278668
- NotebookLM 帮助：https://support.google.com/notebooklm/
- Perplexity：https://www.perplexity.ai/
- Perplexity 帮助中心：https://www.perplexity.ai/help-center/

### 开发环境

- Chrome：https://www.google.com/chrome/
- Git：https://git-scm.com/install/
- VS Code：https://code.visualstudio.com/Download
- VS Code 系统要求：https://code.visualstudio.com/docs/supporting/requirements
- Python：https://www.python.org/downloads/
- Node.js LTS：https://nodejs.org/en/download
- Cursor：https://www.cursor.com/downloads
- Microsoft WSL：https://learn.microsoft.com/windows/wsl/install

---

版本维护建议：每次开课前 7 天由助教检查一次所有链接、系统要求、账号计划和地区可用性；不要把“当前可用”写成长期承诺。
