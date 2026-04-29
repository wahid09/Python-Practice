import asyncio
import time

# async def say_hello():
#     print("Hello...")
#     await asyncio.sleep(2)   # Simulate I/O delay (non-blocking)
#     print("...World!")
#
# async def main():
#     await say_hello()
#
# # Run the async program
# asyncio.run(main())


async def fetch_data(url: str, delay: float):
    print(f"Fetching {url}...")
    await asyncio.sleep(delay)   # Simulate network delay
    print(f"✅ Done: {url}")
    return f"Data from {url}"

async def main():
    start = time.time()

    # Run all three tasks concurrently
    results = await asyncio.gather(
        fetch_data("https://api1.com", 2),
        fetch_data("https://api2.com", 1.5),
        fetch_data("https://api3.com", 1),
    )

    print("All results:", results)
    print(f"Total time: {time.time() - start:.2f} seconds")

asyncio.run(main())