import logging

import requests
from tqdm import tqdm


def get_size(url):
    response = requests.head(url)
    size = int(response.headers["Content-Length"])
    return size


def download_large_file(url: str, destination: str):
    total_size = get_size(url)  # total size in bytes
    chunk_size = int(100e6)  # size of 1 chunk to download 100000000 = 100 MB
    logging.info(f"start downloading from {url}")
    with requests.get(url, stream=True, allow_redirects=True) as r:
        r.raise_for_status()
        with open(destination, "wb") as f:
            for chunk in tqdm(r.iter_content(chunk_size=chunk_size), total=total_size // chunk_size):
                f.write(chunk)
    logging.info(f"downloaded to {destination}")
    return destination
