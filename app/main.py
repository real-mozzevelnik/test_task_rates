from fastapi import FastAPI
from app.rates.router import router as rates_router
from app.insurances.router import router as insurances_router
from app.middlewares.logging import LoggingMiddleware
from app.kafka.kafka import producer

app = FastAPI()
logging = LoggingMiddleware(
    producer=producer,
    endpoints=[
        '/rates/'
    ]
)
app.middleware("http")(logging)

@app.on_event("startup")
async def startup_event():
    await producer.start()

@app.on_event("shutdown")
async def shutdown_event():
    await producer.stop()

@app.get('/hello')
async def hello():
    return 'hello world!'

app.include_router(rates_router)
app.include_router(insurances_router)