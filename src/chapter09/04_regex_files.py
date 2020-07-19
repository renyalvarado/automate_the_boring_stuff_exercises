#! /usr/bin/env python3
# Regex Search
"""Program: Regex Search
    Usage: ./04_regex_files.py dir

    Parameters:
    dir: Directory where we search pattern in text files (with .txt extension)
"""

import re
import sys
from pathlib import Path

print("Regex Search")
if len(sys.argv) < 2:
    print(__doc__)

# I use /usr/share/doc/syslinux-common/asciidoc/ in order to test
my_dir = Path(sys.argv[1])
if not my_dir.exists():
    print(f"Error. Directory '{sys.argv[1]}' does not exist", file=sys.stderr)
    exit(1)

my_pattern = re.compile(r"(work)")

for my_file in my_dir.glob("*.txt"):
    a = my_file.read_text()
    for line in a.split("\n"):
        if my_pattern.search(line):
            new_line = re.sub(my_pattern, r"_______\1_______", line)
            print(f"{my_file}: {new_line}")
