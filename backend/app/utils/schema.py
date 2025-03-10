from sqlalchemy import Column, Integer, String, Float

from app.utils.database import Base

# 食材テーブルの定義
class Food(Base):
    """食材テーブルの定義"""
    
    # テーブル名を指定
    __tablename__ = "foods"
    
    # カラム定義
    id = Column(Integer, primary_key=True, index=True)  # 主キー（自動採番）
    name = Column(String, index=True)  # 食材名
    price = Column(Float)  # 100gあたりの価格（円）
    calories = Column(Float)  # 100gあたりのカロリー（kcal）
    protein = Column(Float)  # タンパク質（g/100g）
    fat = Column(Float)  # 脂質（g/100g）
    carbohydrate = Column(Float)  # 炭水化物（g/100g）
    vitamin = Column(Float)  # ビタミン含有量（相対値）
    mineral = Column(Float)  # ミネラル含有量（相対値）
    category = Column(String)  # 食材カテゴリ
    
    def __repr__(self):
        """出力用の文字列表現"""
        return f"<Food(id={self.id}, name='{self.name}', category='{self.category}')>"