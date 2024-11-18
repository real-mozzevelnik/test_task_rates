from pydantic import BaseModel, Field
from datetime import date as Date

class GetInsurancePrice(BaseModel):
    date: Date = Field(description="Дата перевозки")
    cargo_type: str = Field(description="Тип груза")
    price: float = Field(description="Цена товара") 