#! /usr/bin/env python3
# Opening All Search Results

import re
import sys
import bs4
import requests
import webbrowser

print("Searching...")
my_url = f"https://google.com/search?q=https://pypi.org/search/?q={' '.join(sys.argv[1:])}"
res = requests.get(my_url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
link_elements = soup.select("div.ZINbbc > div.kCrYT > a")
print(link_elements)
my_link_re = re.compile(r"http.*/")
for link_element in link_elements:
    href = link_element.attrs.get("href")
    my_url = my_link_re.search(href)
    if my_url:
        print('Opening', my_url.group())
        webbrowser.open(my_url.group())
print("End")
