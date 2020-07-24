# ! /usr/bin/env python3
# Download book

import sys
import requests

try:
    res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
    res.raise_for_status()
    print("First lines of Romeo and Juliet")
    for i, line in enumerate(res.iter_lines(decode_unicode=True)):
        if i > 15:
            break
        print(line)
    play_filename = "romeo_and_juliet.txt"
    with open(play_filename, "wb") as r:
        for chunk in res.iter_content(100_000):
            r.write(chunk)
        print(f"Book saved in '{play_filename}'")
except Exception as e:
    print(e, file=sys.stderr)
