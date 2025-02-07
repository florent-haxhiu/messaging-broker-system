import asyncio

from websockets.asyncio.server import serve


async def echo(ws):
    async for message in ws:
        await ws.send(message)


async def main():
    async with serve(echo, "localhost", 5678):
        await asyncio.get_running_loop().create_future()


asyncio.run(main())
