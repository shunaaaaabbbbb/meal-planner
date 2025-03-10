# 貢献ガイドライン

このプロジェクトへの貢献を検討していただきありがとうございます。以下のガイドラインに従って、スムーズな開発プロセスを維持しましょう。

## 開発フロー

このプロジェクトでは GitHub Flow を採用しています:

1. `main` ブランチから新しいブランチを作成
2. 変更を実装
3. プルリクエストを作成
4. レビューとフィードバック
5. `main` ブランチにマージ

## ブランチ命名規則

ブランチ名は以下の形式で作成してください：

```
<type>/<short-description>
```

例：
- `feature/add-nutrition-chart`
- `bugfix/fix-optimization-algorithm`
- `docs/update-installation-guide`

## コミットメッセージのガイドライン

コミットメッセージは[Conventional Commits](https://www.conventionalcommits.org/)に従ってください：

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

例：
- `feat(optimizer): 栄養バランス最適化アルゴリズムの実装`
- `fix(ui): カロリーグラフの表示バグを修正`
- `docs: インストール手順を更新`

## プルリクエスト

プルリクエスト（PR）を作成する際は、以下のテンプレートに従ってください：

- 変更の概要を簡潔に説明
- 実装の詳細
- 関連するIssue番号
- テスト方法

## コード品質

以下のツールを使用してコード品質を維持しています：

- **Python**: flake8, black, isort
- **JavaScript/React**: ESLint, Prettier

コミット前に `pre-commit` フックが自動的にこれらのチェックを実行します。

## テスト

新しい機能を追加する場合は、対応するテストも追加してください：

- **バックエンド**: pytest を使用
- **フロントエンド**: Jest を使用

## ドキュメント

コードには適切なドキュメントを追加してください：

- **Python**: docstring (Google スタイル)
- **JavaScript/React**: JSDoc

## 質問がある場合

質問やサポートが必要な場合は、Issue を作成するか、プロジェクト管理者に連絡してください。