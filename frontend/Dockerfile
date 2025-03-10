FROM node:16-alpine

WORKDIR /app

# package.jsonをコピー
COPY package.json ./

# 依存関係をインストール
RUN npm install

# アプリケーションコードをコピー
COPY . .

# 開発用ポートを公開
EXPOSE 3000

# 開発サーバー起動
CMD ["npm", "start"]