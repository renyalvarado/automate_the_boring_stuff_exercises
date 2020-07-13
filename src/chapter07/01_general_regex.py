#! /usr/bin/env python3
# General test using regex
import re

telephone_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = telephone_regex.search("My number is 415-555-4242.")
print("Phone number found: " + mo.group())

telephone_regex2 = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
mo2 = telephone_regex2.search("My number is 415-555-4242.")
print(f"Phone number found2: {mo2.group()} + {mo2.groups()}" if mo2 else "Not found")
