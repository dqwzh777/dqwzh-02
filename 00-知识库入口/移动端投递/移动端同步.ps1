param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('主库', '投递', '发布', '状态')]
    [string]$动作
)

$ErrorActionPreference = 'Stop'
$投递目录 = '00-知识库入口/移动端投递'

function 确认工作区干净 {
    $状态 = @(git status --porcelain | Where-Object { $_ -notmatch '__pycache__' })
    if ($状态.Count -gt 0) {
        throw "工作区有未提交内容。请先运行发布动作，或手动处理后再切换。"
    }
}

switch ($动作) {
    '主库' {
        确认工作区干净
        git switch main
        git pull --ff-only origin main
        Write-Output '已更新到主库 main：只读浏览和检索请在此分支进行。'
    }
    '投递' {
        确认工作区干净
        git switch windows-inbox
        git fetch origin windows-inbox
        git rebase origin/windows-inbox
        Write-Output "已进入 windows-inbox：请只在 $投递目录 中新增临时任务、信息或文件。"
    }
    '发布' {
        $当前分支 = git branch --show-current
        if ($当前分支 -ne 'windows-inbox') {
            throw '发布前请先运行：.\移动端同步.ps1 投递'
        }
        git add -- $投递目录
        git diff --cached --quiet
        if ($LASTEXITCODE -eq 0) {
            Write-Output '投递目录没有新的可发布内容。'
            exit 0
        }
        $时间 = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
        git commit -m "mobile inbox: $时间"
        git push origin windows-inbox
        Write-Output '已推送 windows-inbox；macOS 主机下次每日收件时会读取。'
    }
    '状态' {
        git status --short --branch
        git log --oneline -3
    }
}
