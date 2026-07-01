---
engine: copilot
on:
  schedule:
    - cron: 'weekly on monday'
  workflow_dispatch:
permissions:
  contents: read
tools:
  cli-proxy: true
safe-outputs:
  create-pull-request:
    draft: false
---

# READMEの自動アップデートエージェント

このリポジトリの最新のコードベース、コミット履歴、および最近クローズされたIssueやPRを確認してください。
現在のソースコードの実装状況と、現在の README.md の記述内容に乖離がないか検証してください。
