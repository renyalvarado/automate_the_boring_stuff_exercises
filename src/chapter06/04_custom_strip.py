#! /usr/bin/env python3
# Custom version of string method "strip"
import re


def custom_strip(my_string: str, chr_to_delete: str = " ") -> str:
    special_characters = "[]^-"
    if chr_to_delete in special_characters:
        chr_to_delete = "\\" + chr_to_delete
    str_regex = f"{chr_to_delete}*([^{chr_to_delete}]*){chr_to_delete}*"
    cleaner_regex = re.compile(str_regex)
    clean_match = cleaner_regex.match(my_string)
    a = clean_match.group(1)
    return a


print(custom_strip(" Hello World"))
print(custom_strip("---44444---", "-"))
