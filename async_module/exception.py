# import asyncio
#
# async def risky_task():
#     await asyncio.sleep(1)
#     raise ValueError("Something went wrong!")
#
# async def main():
#     try:
#         await risky_task()
#     except ValueError as e:
#         print(f"Caught error: {e}")
#
# asyncio.run(main())
#
# results = await asyncio.gather(
#     risky_task(), risky_task(),
#     return_exceptions=True
# )

import asyncio

class AsyncDownloader:
    def __init__(self):
        self.session = None

    async def __aenter__(self):
        import aiohttp
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *args):
        await self.session.close()

    async def download(self, url):
        async with self.session.get(url) as resp:
            return await resp.text()

# Usage:
async def main():
    async with AsyncDownloader() as downloader:
        data = await downloader.download("https://example.com")