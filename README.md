# 献立最適化アプリ

数理最適化技術を用いて栄養バランスの取れた献立を提案するアプリケーション

## 概要
このアプリケーションは、線形計画法（PuLP）を用いて、予算やカロリー制限などの制約条件の下で最適な献立を提案します。

### 主な機能
- 栄養バランスの最適化
- 予算内での食材選択
- 5大栄養素の摂取量をグラフで可視化
- カロリー管理

## 技術スタック
- **バックエンド**: Python, FastAPI, PuLP
- **フロントエンド**: React, Material-UI, Chart.js
- **データベース**: SQLite
- **開発環境**: Docker
- **テスト**: pytest
- **CI/CD**: GitHub Actions

## 開発環境のセットアップ

### 前提条件
- Docker と Docker Compose がインストールされていること
- Git がインストールされていること

### セットアップ手順

```bash
# リポジトリをクローン
git clone https://github.com/yourusername/meal-planner.git
cd meal-planner

# Dockerコンテナを起動
docker-compose up -d

# バックエンドの開発サーバーにアクセス
http://localhost:8000

# フロントエンドの開発サーバーにアクセス
http://localhost:3000
```

## 開発ガイドライン
詳細な開発ガイドラインは [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

## ライセンス
このプロジェクトは MIT ライセンスの下で公開されています。