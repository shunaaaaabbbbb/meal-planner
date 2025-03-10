from pydantic import BaseModel, Field

class Food(BaseModel):
    """食材データモデル

    Attributes:
        id: 食材ID
        name: 食材名
        price: 100gあたりの価格（円）
        calories: 100gあたりのカロリー（kcal）
        protein: 100gあたりのタンパク質（g）
        fat: 100gあたりの脂質（g）
        carbohydrate: 100gあたりの炭水化物（g）
        vitamin: 100gあたりのビタミン含有量（相対値）
        mineral: 100gあたりのミネラル含有量（相対値）
        category: 食材カテゴリ
    """

    id: int
    name: str
    price: float = Field(..., ge=0)
    calories: float = Field(..., ge=0)
    protein: float = Field(..., ge=0)
    fat: float = Field(..., ge=0)
    carbohydrate: float = Field(..., ge=0)
    vitamin: float = Field(..., ge=0)
    mineral: float = Field(..., ge=0)
    category: str


class FoodCreate(BaseModel):
    """食材データ作成モデル"""

    name: str
    price: float = Field(..., ge=0)
    calories: float = Field(..., ge=0)
    protein: float = Field(..., ge=0)
    fat: float = Field(..., ge=0)
    carbohydrate: float = Field(..., ge=0)
    vitamin: float = Field(..., ge=0)
    mineral: float = Field(..., ge=0)
    category: str

class FoodResponse(Food):
    """食材レスポンスモデル"""
    class Config:
        """Pydanticモデル設定"""
        orm_mode = True  # SQLAlchemyモデルからの変換を可能にする