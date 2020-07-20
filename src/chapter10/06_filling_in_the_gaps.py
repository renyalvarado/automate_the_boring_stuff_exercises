# ! /usr/bin/env python3
# Filling in the Gaps
import operator
import re


def compare_tri(x, y):
    return int(x.get(1)) < int(y.get(1))


prefix = "spam"

file_pattern = re.compile("^(" + prefix + r")(\d{3})(.*?)$")

files = ["spam003.txt", "spam001.txt", "bruno", "spam010.txt"]
selected_files = []
min_number = 1000
for f in files:
    file_re_result = file_pattern.search(f)
    if file_re_result:
        selected_files.append(
            (file_re_result.group(1), file_re_result.group(2), file_re_result.group(3), file_re_result.group(0),)
        )
        file_number = int(file_re_result.group(2))
        if file_number < min_number:
            min_number = file_number

for f in sorted(selected_files, key=operator.itemgetter(1)):
    new_file_name = f"{f[0]}{str(min_number).zfill(3)}{f[2]}"
    old_file_name = f[3]
    min_number += 1
    print(f"{old_file_name} -> {new_file_name}")
