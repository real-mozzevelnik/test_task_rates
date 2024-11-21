from pydantic import BaseModel, Field
from typing import List
from datetime import date as Date

class RatesUpsertDataObject(BaseModel):
    date: Date = Field(description="Дата перевозки")
    cargo_type: str = Field(description="Тип груза")
    rate: float = Field(description="Тариф")
    
class RatesUpsert(BaseModel):
    rates: List[RatesUpsertDataObject] = Field(description="Список тарифов")
    user_id: str


class RatesDeleteDataObject(BaseModel):
    date: Date = Field(description="Дата перевозки")
    cargo_type: str = Field(description="Тип груза")

class RatesDelete(BaseModel):
    rates: List[RatesDeleteDataObject] = Field(description="Список тарифов")
    user_id: str