import concurrent.futures
import requests
import threading
import time


thread_local = threading.local()
# .local looks at each individual thread


def get_session():
    # session I look up is specific to the thread which I'm running on.
    if not hasattr(thread_local, "session"):
        # I create a session the first time I get called in a specific thread.
        thread_local.session = requests.Session()
    # use that session on each subsequent call
    return thread_local.session


def download_site(url):
    session = get_session() # call above function
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # it creates a pool of threads
        # and controls how and when each threads in the pool run
        # Some experimentation is required: max_workers
        executor.map(download_site, sites)
        # .map runs the passed-in function on each of the sites in the list


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")