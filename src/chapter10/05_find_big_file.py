# ! /usr/bin/env python3
# Find Big Files

import os
import sys
from pathlib import Path

MAX_FILE_SIZE = 100 * 1024 * 1024

broken_files = []
show_broken = False
for folder_name, _, file_names in os.walk(Path.home(), followlinks=False):
    for filename in file_names:
        str_path = f"{folder_name}/{filename}"
        try:
            full_path = Path(str_path)
            file_size = os.path.getsize(full_path)
            if file_size > MAX_FILE_SIZE:
                print(full_path, f"{file_size // (1024 * 1024)}MB")
        except FileNotFoundError:
            broken_files.append(str_path)
if show_broken:
    for f in broken_files:
        print("\n".join(broken_files), file=sys.stderr)
