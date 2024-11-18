from fastapi import APIRouter 
from starlette import status
from starlette.responses import Response
from app.rates.schemas import RatesUpsert, RatesDelete
from app.rates.service import RatesService


router = APIRouter(prefix='/rates', tags=['Работа с тарифами'])

    
@router.post("/", summary="Добавить или изменить тарифы")
async def upsert_rates(body: RatesUpsert):
    await RatesService.upsert_rates(body)
    return Response(status_code=status.HTTP_200_OK)
    
@router.delete("/", summary="Удалить тарифы")
async def upsert_rates(body: RatesDelete):
    await RatesService.delete_rates(body)
    return Response(status_code=status.HTTP_200_OK)