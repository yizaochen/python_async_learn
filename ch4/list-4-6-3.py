import asyncio
import aiohttp
from util import async_timed, fetch_status


@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        urls = ["https://www.example.com", "python://example.com"]
        requests = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*requests, return_exceptions=True)

        exceptions = [res for res in results if isinstance(res, Exception)]
        successful_results = [res for res in results if not isinstance(res, Exception)]
        
        print(f"All results: {results}")
        print(f"Finished successfully: {successful_results}")
        print(f"Threw exceptions: {exceptions}")


asyncio.run(main())
