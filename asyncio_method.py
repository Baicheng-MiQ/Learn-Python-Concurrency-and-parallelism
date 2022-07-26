import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        return await response.json()

async def download_all_sites(sites):
    # can share the session across all tasks, so
    # the session is created as a context manager.
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
                        # takes care of starting them
            tasks.append(task)
        # limit the number of concurrent tasks to 8
        semaphore = asyncio.Semaphore(8)

        async def sem_task(task_):
            async with semaphore:
                return await task_

        # finally run the tasks
        original_result = await asyncio.gather(*(sem_task(task) for task in tasks))
        # keep the session context alive until all the tasks have completed.
    return original_result


if __name__ == "__main__":
    sites = [
        "https://digital.ucas.com/coursedisplay/autocomplete?searchTerm=ucl",
    ] * 80
    start_time = time.time()
    result = asyncio.run(download_all_sites(sites))
    # in older versions of python: asyncio.get_event_loop().run_until_complete()
    print(result)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")