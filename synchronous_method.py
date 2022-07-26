import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {response.json()} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        # Session object allows requests to do some fancy networking tricks
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://digital.ucas.com/coursedisplay/autocomplete?searchTerm=peking",
    ] * 8
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")