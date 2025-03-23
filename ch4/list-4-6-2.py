import asyncio
import aiohttp
from util import async_timed, fetch_status


@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        urls = ["https://www.example.com", "python://example.com"]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


asyncio.run(main())
