# ! /usr/bin/env python3
# Parsing HTML with the bs4 Module

import bs4

print("Parsing HTML with the bs4 Module")
html_filename = "example.html"
print(f"Parsing file '{html_filename}'")

with open(html_filename) as h:
    example_soup = bs4.BeautifulSoup(h, "html.parser")
    paragraphs = example_soup.select("p")
    print("**************************************")
    print("Listing paragraphs content")
    for p in paragraphs:
        print(f"paragraph -> \n{str(p)}\n\n")
    print("**************************************")
