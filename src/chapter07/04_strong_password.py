#! /usr/bin/env python3
# Detect strong password

import re

length_regex = re.compile(r".{8,}")
at_least_upper_regex = re.compile(r"[A-Z]+")
at_least_lowe_regex = re.compile(r"[a-z]+")
at_least_digit = re.compile(r"\d+")


def is_strong_password(my_password: str) -> bool:
    return bool(length_regex.search(my_password) and at_least_upper_regex.search(my_password)
                and at_least_lowe_regex.search(my_password) and at_least_digit.search(my_password))


password_list = ["a", "Asdfds", "dsfdf3434", "dsfdf3434A"]

for p in password_list:
    print(f"Is '{p}' a strong password? -> {is_strong_password(p)}")
