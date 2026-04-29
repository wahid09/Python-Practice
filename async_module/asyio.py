import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/1.5"
    ]

    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)

    print(f"Fetched {len(results)} pages")

asyncio.run(main())

async def background_task(name: str):
    await asyncio.sleep(2)
    print(f"Background task {name} completed")

async def main():
    # Create tasks (they start running immediately)
    task1 = asyncio.create_task(background_task("A"))
    task2 = asyncio.create_task(background_task("B"))

    print("Main function continues...")
    await asyncio.sleep(1)
    print("Main is still running while tasks are in background")

    # Wait for them if needed
    await task1
    await task2

asyncio.run(main())