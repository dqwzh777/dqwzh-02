---
tags:
  - git
  - github
  - obsidian
created: 2026-07-07
---

# 如何使用 Github 同步 Obsidian

## 当前状态

- 本地笔记库路径：`/Users/mac/Documents/Obsidian Vault`
- 本地 Git 仓库：已初始化
- GitHub 仓库：`dqwzh777/dqwzh-02`
- 远端地址：`https://github.com/dqwzh777/dqwzh-02.git`
- Git 用户名：`王利`
- Git 邮箱：`dqwzh777@gmail.com`
- Obsidian Git 插件：已放入插件目录并加入启用列表

## 还差的最后一步

本地仓库已经绑定到 GitHub 的 `DQWZH-02` 仓库，但当前电脑还没有可用的 GitHub 推送凭证。

可以二选一：

- HTTPS：登录 GitHub 凭证或配置 Personal Access Token。
- SSH：把本机 SSH 公钥添加到 GitHub 后，把远端切换成 SSH 地址。

## 当前已完成的本地连接

当前已经执行过：

```bash
cd "/Users/mac/Documents/Obsidian Vault"
git remote add origin https://github.com/dqwzh777/dqwzh-02.git
git branch -M main
```

凭证配置好后，只需要执行：

```bash
git push -u origin main
```

## Obsidian 里怎么同步

1. 重启 Obsidian。
2. 打开设置，进入第三方插件，确认 `Obsidian Git` 已启用。
3. 打开命令面板，运行 `Git: Commit-and-sync`。
4. 以后可以在插件设置里打开自动备份，例如每 10 分钟提交一次。

## 建议

- 仓库设为 Private，避免个人笔记公开。
- 第一次推送前确认 `.gitignore` 已生效。
- 如果多设备同步，先 Pull 再写笔记，减少冲突。
