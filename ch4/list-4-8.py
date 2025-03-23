import asyncio
import aiohttp
from util import async_timed, fetch_status


@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://www.example.com', 1),
            fetch_status(session, 'https://www.example.com', 3),
            fetch_status(session, 'https://www.example.com', 10),
        ]

        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)

asyncio.run(main())
