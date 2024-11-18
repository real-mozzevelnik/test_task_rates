from fastapi import APIRouter 
from starlette import status
from starlette.responses import JSONResponse
from app.insurances.schemas import GetInsurancePrice
from app.insurances.service import InsurancesService


router = APIRouter(prefix='/insurances', tags=['Работа со страхованием'])

    
@router.post("/calculate", summary="Получение стоимости страхования")
async def get_insurance_price(body: GetInsurancePrice):
    insurance_price = await InsurancesService.get_insurance_price(body)
    if insurance_price == None:
        response = {
            "error": "No rate found for this date and cargo_type"
        }
        return JSONResponse(content=response ,status_code=status.HTTP_400_BAD_REQUEST)
    response = {
        "insurance_price": insurance_price
    }
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
