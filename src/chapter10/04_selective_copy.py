# ! /usr/bin/env python3
# Selective Copy
import os
import shutil
import sys
import tempfile
from pathlib import Path


def get_new_filename(old_file_name: Path, new_dir: Path) -> Path:
    candidate = new_dir / old_file_name.name
    if not candidate.exists():
        return candidate
    i = 1
    while True:
        new_candidate = new_dir / f"{old_file_name.stem}{i}{old_file_name.suffix}"
        if not new_candidate.exists():
            return new_candidate
        i += 1


print("Selective Copy")

source_backup_dir = Path("/usr/share/doc/syslinux-common")

destiny_backup_dir = Path(tempfile.gettempdir()) / "my_backup_dir"

if not destiny_backup_dir.exists():
    print(f"Error. Directory {str(destiny_backup_dir)} does not exist", file=sys.stderr)
    exit(1)

for folder_name, _, file_names in os.walk(source_backup_dir):
    for filename in file_names:
        full_path = Path(f"{folder_name}/{filename}")
        new_path = get_new_filename(full_path, destiny_backup_dir)
        shutil.copy(full_path, new_path)
        print(full_path)

print(destiny_backup_dir)
