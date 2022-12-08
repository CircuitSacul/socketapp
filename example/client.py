import asyncio

from example.events import Message
from socketapp import Client


async def send(client: Client) -> None:
    await client.wait_until_ready()
    while True:
        await client.send(Message(data="hi"), client.clients)
        await asyncio.sleep(1)


async def main(client: Client) -> None:
    asyncio.create_task(send(client))
    await client.run()


try:
    client = Client()
    asyncio.run(main(client))
finally:
    client.stop()
