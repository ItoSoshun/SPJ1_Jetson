---
engine: copilot
on:
  schedule:
    - cron: 'weekly on monday'
  workflow_dispatch:
permissions:
  contents: read
tools:
  # 🔽 エージェントにリポジトリ内のファイルを読み書きさせる必須ツール
  - name: github-contents
  # 🔽 エージェントにプルリクエストを自動作成させる必須ツール
  - name: github-pull-requests
safe-outputs:
  create-pull-request:
    draft: false
---

# READMEの全自動作成エージェント

## タスク
リポジトリ内にある `py` フォルダの中身（Pythonソースコード）をすべて読み込み、そのプログラムの機能や使い方を詳しく解析してください。

## 成果物
解析した結果を基に、リポジトリのトップ階層にある `README.md` へ詳細なドキュメント（概要、機能一覧、使い方など）を記述し、プルリクエスト（Pull Request）を作成してください。
現在のREADMEが空であるため、必ず新規にドキュメントを生成してください。
