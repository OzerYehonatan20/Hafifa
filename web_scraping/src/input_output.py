import json
import os


#input
def read_urls(file_path: str) -> list[str]:
    # read the file urls.input and return a list of urls
    urls = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            url = line.strip()
            if url:
                urls.append(url)
    return urls

