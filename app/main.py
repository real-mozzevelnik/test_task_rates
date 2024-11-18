from fastapi import FastAPI
from app.rates.router import router as rates_router
from app.insurances.router import router as insurances_router

app = FastAPI()

@app.get('/hello')
async def hello():
    return 'hello world!'

app.include_router(rates_router)
app.include_router(insurances_router)