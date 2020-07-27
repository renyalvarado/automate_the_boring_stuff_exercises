#! /usr/bin/env python3
# Downloading All XKCD Comics with threads

import re
import bs4
import pathlib
import threading
import requests

print("Downloading All XKCD Comics")


def get_xkcd_image_url(min_number, max_number):
    print(f"Downloading image from {min_number} to {max_number}")
    base_xkcd = "https://xkcd.com"
    protocol = re.compile("https?").search(base_xkcd).group()
    for i in range(min_number, max_number + 1):
        current_url = f"https://xkcd.com/{i}/"
        res = requests.get(current_url)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        img_element = soup.select_one("#comic img")
        img_url = f"{protocol}:{img_element.attrs.get('src')}"
        res_img = requests.get(img_url, timeout=10)
        filename = "xkcd/" + img_url.split('/')[-1]
        with open(filename, "wb") as f:
            for chunk in res_img.iter_content(10000):
                f.write(chunk)


xkcd_img_folder = pathlib.Path("xkcd")
xkcd_img_folder.mkdir(parents=True, exist_ok=True)

my_threads = []
for i in range(4):
    t = threading.Thread(target=get_xkcd_image_url, args=((i * 5) + 1, (i * 5) + 5))
    t.start()
    my_threads.append(t)

for my_thread in my_threads:
    my_thread.join()

print("\nDone!")
