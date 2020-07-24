#! /usr/bin/env python3
# Downloading All XKCD Comics

import re
import bs4
from pathlib import Path
import requests

print("Downloading All XKCD Comics")


def get_xkcd_info(current_url):
    base_xkcd = "https://xkcd.com"
    protocol = re.compile("https?").search(base_xkcd).group()
    ready_to_go = True
    while ready_to_go:
        res = requests.get(current_url)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        img_element = soup.select_one("#comic img")
        img_url = f"{protocol}:{img_element.attrs.get('src')}"
        previous_element = soup.select_one("a[rel='prev']")
        previous_href = previous_element.attrs.get('href')
        previous_url = f"{base_xkcd}{previous_href}"
        yield current_url, img_url
        current_url = previous_url
        if previous_href == "#":
            ready_to_go = False


xkcd_img_folder = Path("xkcd")
xkcd_img_folder.mkdir(parents=True, exist_ok=True)

for current_url, img_url in get_xkcd_info("https://xkcd.com/6/"):
    print(current_url)
    print(img_url)
    res_img = requests.get(img_url, timeout=10)
    filename = "xkcd/" + img_url.split('/')[-1]
    with open(filename, "wb") as f:
        for chunk in res_img.iter_content(10000):
            f.write(chunk)
