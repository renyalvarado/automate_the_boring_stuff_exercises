# ! /usr/bin/env python3
# Backing Up a Folder into a ZIP File

import itertools
import os
import tempfile
import zipfile
from pathlib import Path

destiny_backup_dir = Path(tempfile.gettempdir())
BASE_BACKUP_NAME = "backup"
backup_dir = "/usr/share/doc/syslinux-common"


def get_new_backup_name(base_dir: Path, base_filename: str) -> Path:
    for i in itertools.count(1):
        new_name = base_dir / f"{base_filename}{i}.zip"
        if not new_name.exists():
            return new_name


def copy_dir_to_zip(base_dir: Path, zip_file):
    for folder_name, _, filenames in os.walk(base_dir):
        for filename in filenames:
            full_path = f"{folder_name}/{filename}"
            relative_path = os.path.relpath(full_path, base_dir)
            print(f"{base_dir}; {folder_name}; {full_path}; {relative_path}")
            zip_file.write(full_path, relative_path)


backup_filename = get_new_backup_name(destiny_backup_dir, BASE_BACKUP_NAME)
print(backup_filename)
with zipfile.ZipFile(backup_filename, 'w') as backup_zipfile:
    copy_dir_to_zip(backup_dir, backup_zipfile)
