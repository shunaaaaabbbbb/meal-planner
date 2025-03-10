from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLiteデータベースのURL
# SQLiteではファイルパスがデータベースの場所になる
SQLALCHEMY_DATABASE_URL = "sqlite:///./meal_planner.db"

# エンジンを作成
# check_same_thread=False はSQLiteの場合のみ必要
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# セッションファクトリーを作成
# autocommit=False: コミットは手動で行う
# autoflush=False: クエリ実行時に自動でフラッシュしない
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデルの基底クラス
Base = declarative_base()

# FastAPIの依存性注入で使用するDB取得関数
def get_db():
    db = SessionLocal()
    try:
        yield db  # リクエスト処理中はDBセッションを提供
    finally:
        db.close()  # リクエスト終了後に必ずセッションを閉じる