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

## 目的
- 新しい機能や設定、コンポーネントが追加されているのに README.md に記載がない場合は、適切にドキュメントを追記してください。
- 変更された古い仕様や、不要になった設定手順の記述があれば、最新のコードに合わせて修正してください。

## 成果物
変更が必要であると判断した場合は、変更理由を記した適切なコミットメッセージを設定し、プルリクエスト（Pull Request）を作成してください。
特に変更が必要ない（すでに最新の状態である）と判断した場合は、何も変更を行わずにそのまま終了してください。 
