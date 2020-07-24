# ! /usr/bin/env python3
# Map It!

import sys
import webbrowser
import pyperclip

print("Map it!")
base_map_url = "https://www.google.com/maps/place/"
address = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else pyperclip.paste()
webbrowser.open(base_map_url + address)
