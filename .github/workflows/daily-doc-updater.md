---
engine: copilot
on:
  schedule:
    - cron: 'weekly on monday'
  workflow_dispatch:
permissions:
  contents: read
tools:
  - github-contents
  - github-pull-requests
# 🔽 安全装置を「確認なしで即時プルリク作成・送信」に強制変更します
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
