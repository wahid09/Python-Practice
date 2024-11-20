from timeit import default_timer
import aiohttp
import asyncio

async def load_data(session, delay):
    print(f'Starting {delay} second timer')
    async with session.get(f'https://httpbin.org/delay/{delay}') as resp:
        text = await resp.text()
        print(f'Completed {delay} second timer')
        return text

async def main():
    start_time = default_timer()
    async with aiohttp.ClientSession() as session:
        two_task = asyncio.create_task(load_data(session, 2))
        three_task = asyncio.create_task(load_data(session, 3))

        await asyncio.sleep(1)
        two_result = await two_task
        three_result = await three_task

        elapsed_time = default_timer() - start_time
        print(f'The operation took {elapsed_time: .2} second')


asyncio.run(main())

