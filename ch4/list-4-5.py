import asyncio
from util import async_timed, delay


@async_timed()
async def main() -> None:
    delay_times = [3, 3, 3]
    tasks = [asyncio.create_task(delay(delay_time)) for delay_time in delay_times]
    [await task for task in tasks]


asyncio.run(main())
