#! /usr/bin/env python3
# Downloading Images from Flickr

import re
import bs4
from pathlib import Path
import requests

current_url = "https://www.flickr.com/search/?text=dogs"
protocol = re.compile("https?").search(current_url).group()
res = requests.get(current_url)
soup = bs4.BeautifulSoup(res.text, "html.parser")
div_images = soup.select("div.view.photo-list-photo-view")
valid_images = 0
image_regex = re.compile(r"url\((.*)\)")

xkcd_img_folder = Path("flickr")
xkcd_img_folder.mkdir(parents=True, exist_ok=True)

for div_image in div_images:
    style_image = div_image.attrs.get("style")
    if style_image:
        image_url_style = image_regex.search(style_image)
        if image_url_style:
            valid_images += 1
            img_url = f"{protocol}:{image_url_style.group(1)}"
            print(img_url)
            res_img = requests.get(img_url, timeout=10)
            filename = "flickr/" + Path(img_url).name
            with open(filename, "wb") as f:
                for chunk in res_img.iter_content(10000):
                    f.write(chunk)
    if valid_images > 4:
        break

# print(div_images)
