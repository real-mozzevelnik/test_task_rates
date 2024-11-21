from aiokafka import AIOKafkaProducer
import asyncio
import json
from app.config import settings

event_loop = asyncio.get_event_loop()


class Kafka():
    def __init__(self, bootstrap_server: str, client_id: str):
        self.__producer = AIOKafkaProducer(
            bootstrap_servers=bootstrap_server,
            client_id=client_id,
            loop=event_loop,
        )

    async def start(self):
        await self.__producer.start()

    async def stop(self):
        await self.__producer.stop()

    async def send(self, topic: str, value: dict) -> None:
        await self.__producer.send(
            topic=topic,
            value=json.dumps(value).encode("ascii")
        )


producer = Kafka(bootstrap_server=settings.KAFKA_BOOTSTRAP_SERVER, client_id=settings.KAFKA_CLIENT_ID)
