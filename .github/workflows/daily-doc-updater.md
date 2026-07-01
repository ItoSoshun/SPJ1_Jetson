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

# READMEの自動作成エージェント

## タスク
リポジトリのトップ階層にある `py` フォルダの中身（Pythonソースコード）をすべて読み込み、そのプログラムが「何をするものなのか（機能）」「どのように使うのか（使用方法）」を詳しく解析してください。

## 成果物
解析した結果を基に、リポジトリのトップ階層にある `README.md` へ詳細なドキュメント（概要、機能一覧、使い方など）を**必ず記述・追記**し、プルリクエスト（Pull Request）を作成してください。現在のREADMEが空である場合は、一からドキュメントを生成してください。
