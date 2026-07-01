---
engine: github  # 👈 ここを「copilot」から「github」に変えるのが最大のポイントです！
on:
  schedule:
    - cron: 'weekly on monday'
  workflow_dispatch:
permissions:
  contents: write       # 👈 permissions は両方 write にします
  pull-requests: write
tools:
  - github-contents
  - github-pull-requests
safe-outputs:
  create-pull-request:
    review: false
    draft: false
---

# READMEの全自動作成エージェント

## タスク
リポジトリ内にある `py` フォルダの中身（Pythonソースコード）をすべて読み込み、そのプログラムの機能や使い方を詳しく解析してください。

## 成果物
解析した結果を基に、リポジトリのトップ階層にある `README.md` へ詳細なドキュメント（概要、機能一覧、使い方など）を記述し、プルリクエスト（Pull Request）を作成してください。
現在のREADMEが空であるため、必ず新規にドキュメントを生成してください。
