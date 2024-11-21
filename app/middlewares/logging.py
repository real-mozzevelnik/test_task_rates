from fastapi import Request, Response
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import List
from app.kafka.kafka import Kafka
from app.config import settings
import ast

class Log(BaseModel):
    url: str
    method: str
    start_time: datetime
    process_time: timedelta
    response_status_code: int
    user_id: str | None
    request: dict | None

    def json(self):
        return {
            "url": self.url,
            "method": self.method,
            "start_time": self.start_time.strftime('%d-%m-%Y %H:%M:%S'),
            "process_time": str(self.process_time),
            "response_status_code": self.response_status_code,
            "user_id": self.user_id,
            "request": self.request,
        }
    

class LoggingMiddleware:
    def __init__(
            self,
            producer: Kafka,
            endpoints: List[str],
    ):
        self.producer = producer
        self.endpoints = endpoints

    async def set_body(self, request: Request, body: bytes):
        async def receive():
            return {"type": "http.request", "body": body}
        request._receive = receive
 
    async def get_body(self, request: Request) -> bytes:
        body = await request.body()
        await self.set_body(request, body)
        return body

    async def __call__(self, request: Request, call_next):
        url = request.url.path
        if not url in self.endpoints:
            response: Response = await call_next(request)
            return response

        await self.set_body(request, await request.body())
        request_body = ast.literal_eval((await self.get_body(request)).decode("UTF-8"))

        start_time = datetime.now()
        response: Response = await call_next(request)
        process_time = datetime.now() - start_time
        status_code = response.status_code     
        method = request.method
         
        log = Log(
            url=url,
            method=method,
            start_time=start_time,
            process_time=process_time,
            response_status_code=status_code,
            user_id=request_body.get('user_id', None),
            request=request_body
        )
        await self.producer.send(topic=settings.KAFKA_LOG_TOPIC, value=log.json())
        
        return response