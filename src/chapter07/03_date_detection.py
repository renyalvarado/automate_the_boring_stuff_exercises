#! /usr/bin/env python3
# Date detection

import re

date_regex = re.compile(r"(\d{1,2})/(\d{1,2})/(\d{4})")

text_date = "1/2/2020"

date_matches = date_regex.findall(text_date)
if date_matches:
    day, month, year = date_matches[0]
    int_day = int(day)
    int_month = int(month)
    int_year = int(year)
    if (int_day > 0) and (int_day < 32) and (int_month > 0) and (int_month < 13) and (int_year > 0):
        print(f"day: {day.zfill(2)}, month: {month.zfill(2)}, year: {year}")
    else:
        print(f"Bad date: {text_date}")
else:
    print(f"Bad date: {text_date}")
