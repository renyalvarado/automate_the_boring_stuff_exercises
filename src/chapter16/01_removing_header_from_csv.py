#! /usr/bin/env python3
# Removing the Header from CSV Files

import csv
import glob
import pathlib

print("Removing the Header from CSV Files (original_csv directory)")

final_csv_dir = pathlib.Path("final_csv")
for original_csv_filename in glob.glob("./original_csv/*.csv"):
    original_csv_file = pathlib.Path(original_csv_filename)
    with open(original_csv_file) as of:
        original_reader = csv.reader(of)
        final_csv_file = pathlib.Path(final_csv_dir / original_csv_file.name)
        with open(final_csv_file, "w") as ff:
            final_writer = csv.writer(ff)
            for row in original_reader:
                if original_reader.line_num == 1:
                    continue
                final_writer.writerow(row)
            print(f"Original: {original_csv_file.absolute()}")
            print(f"Copy    : {final_csv_file.absolute()}")
            print()
