#! /usr/bin/env python3
# Match all phone numbers and email in clipboard
import re
import pyperclip


def format_phone_number(regex_match):
    new_phone_number = f"{regex_match[1]}-{regex_match[3]}-{regex_match[5]}"
    if regex_match[8]:
        new_phone_number += f" x + {regex_match[8]}"
    return new_phone_number


phone_regex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )""", re.VERBOSE)

email_regex = re.compile(r"""(
   [a-zA-Z0-9._%+-]+      # username
   @                      # @ symbol
   [a-zA-Z0-9.-]+         # domain name
   (\.[a-zA-Z]{2,4})       # dot-something
    )""", re.VERBOSE)

full_text = pyperclip.paste()
phone_number_matches = phone_regex.findall(full_text)
phone_numbers_str = "\n".join([format_phone_number(p) for p in phone_number_matches])
email_matches = email_regex.findall(full_text)
emails_str = "\n".join([e[0] for e in email_matches])
print(full_text)
print("Phone Numbers")
print(phone_numbers_str)
print("Emails")
print(emails_str)

pyperclip.copy(phone_numbers_str + emails_str)
