from sqlalchemy import select, Select
from app.db.database import async_session_maker
from app.db.models.rate import Rate
from app.insurances.schemas import GetInsurancePrice


class InsurancesService:
    @classmethod
    async def get_insurance_price(cls, item_info: GetInsurancePrice) -> int|None:
        async with async_session_maker() as session:
            query: Select = select(Rate).where(Rate.date == item_info.date and Rate.cargo_type == item_info.cargo_type)
            result = await session.execute(query)
            row = result.fetchone()
            if (row == None):
                return None
            else:
                return row[0].rate * item_info.price
