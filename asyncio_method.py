import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    # can share the session across all tasks, so
    # the session is created as a context manager.
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
                        # takes care of starting them
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)
            # keep the session context alive until all the tasks have completed.


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    # in older versions of python: asyncio.get_event_loop().run_until_complete()
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")