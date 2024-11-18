from sqlalchemy.dialects.postgresql import insert, Insert
from sqlalchemy import delete, Delete
from app.db.models.rate import Rate
from app.db.database import async_session_maker
from app.rates.schemas import RatesUpsert, RatesDelete


class RatesService:
    @classmethod
    async def upsert_rates(cls, rates: RatesUpsert):
        async with async_session_maker() as session:
            query: Insert = insert(Rate).values(rates.model_dump()["rates"])
            on_conflict_query = query.on_conflict_do_update(
                index_elements=[Rate.date, Rate.cargo_type], 
                set_=dict(rate=query.excluded.rate, updated_at = query.excluded.updated_at)
            )
            await session.execute(on_conflict_query)
            await session.commit()
        
    @classmethod
    async def delete_rates(cls, rates: RatesDelete):
        async with async_session_maker() as session:
            for rate in rates.rates:
                query: Delete = delete(Rate).where(Rate.date == rate.date and Rate.cargo_type == rate.cargo_type)
                await session.execute(query)
                await session.commit()
