# ! /usr/bin/env python3
# Renaming Files with American-Style Dates to European-Style Dates
import os
import re
import shutil
import tempfile
from pathlib import Path

# Command to create example files
# mkdir /tmp/test_atbs2 && touch /tmp/test_atbs2/{spam4-4-1984.txt,01-03-2014eggs.zip,littlebrother.epub}


date_pattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-                      # one or two digits for the month
    ((0|1|2|3)?\d)-                  # one or two digits for the day
    ((19|20)\d\d)                    # four digits for the year
    (.*?)$                           # all text after the date
""", re.VERBOSE)

my_dir = Path(f"{tempfile.gettempdir()}/test_atbs2/")

for american_filename in os.listdir(my_dir):
    mo = date_pattern.search(american_filename)
    print(my_dir / american_filename)
    if not mo:
        continue
    before = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    after = mo.group(8)
    european_filename = f"{before}{day}-{month}-{year}{after}"
    print(my_dir / european_filename)
    shutil.move(my_dir / american_filename, my_dir / european_filename)
    print()
