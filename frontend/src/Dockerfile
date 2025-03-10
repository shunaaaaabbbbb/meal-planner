FROM node:16-alpine

WORKDIR /app

# 依存関係をコピーしてインストール
COPY package.json package-lock.json ./
RUN npm ci

# アプリケーションコードをコピー
COPY . .

# 開発用ポートを公開
EXPOSE 3000

# 開発サーバー起動
CMD ["npm", "start"]