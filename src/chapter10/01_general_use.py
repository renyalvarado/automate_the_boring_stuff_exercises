import os
import zipfile
import tempfile
from pathlib import Path


# ! /usr/bin/env python3
# Show SYSLINUX documentation
def walk_syslinux_docs():
    for folderName, subfolders, filenames in os.walk("/usr/share/doc/syslinux-common/"):
        print("The current folder is " + folderName)

        for subfolder in subfolders:
            print("SUBFOLDER OF " + folderName + ": " + subfolder)

        for filename in filenames:
            print("FILE INSIDE " + folderName + ": " + filename)

        print("")


# I previously copy a zip into /tmp
def unzip_file(my_zip_filename: Path):
    example_zip = zipfile.ZipFile(my_zip_filename)
    print(f"Zip file ({str(my_zip_filename)}) content")
    for f in example_zip.infolist():
        print(f.filename)
    new_dir = my_zip_filename.parent / my_zip_filename.stem
    example_zip.extractall(new_dir)
    print(f"new dir: {str(new_dir)}")


walk_syslinux_docs()
unzip_file(Path(tempfile.gettempdir()) / "example.zip")
