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

# READMEの全自動作成エージェント

## 前提条件（重要）
このリポジトリのトップ階層には `py` という名前のフォルダがあり、その中にメインのソースコード（Pythonファイル）がすでに格納されています。

## タスク
1. トップ階層にある `py` フォルダの内部をスキャンし、そこにあるすべてのPythonファイル（`.py`）の中身を**すべて1行ずつ読み込んで解析**してください。
2. そのソースコードがどのような処理を行っているか（概要、主な機能、使い方など）を詳細に把握してください。

## 成果物
解析したコードの内容をベースに、リポジトリのトップ階層にある `README.md`（現在は空です）に、開発者向けの詳細なドキュメント（プロジェクト概要、機能一覧、起動方法など）を**新規に必ず執筆**してください。
執筆した内容で、`safe-outputs.create-pull-request` を使用してプルリクエスト（Pull Request）を作成してください。

※「変更の必要がない」という判断は禁止します。READMEが空であるため、必ずドキュメントを生成してください。
