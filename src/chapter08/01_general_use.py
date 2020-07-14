#! /usr/bin/env python3
# Examples of PyInputPlus

import pyinputplus as pyip

my_number = pyip.inputNum(prompt="Give me a positive number: ", min=0)
print(f"number: {my_number}")

max_number = 10
while True:
    int_positive_prompt = f"Give me a positive integer and not greater than {max_number}: "
    my_integer = pyip.inputInt(prompt=int_positive_prompt, min=0, max=max_number, blank=True)
    if my_integer == "":
        if max_number < 60:
            max_number += 10
    else:
        break
print(f"my_integer: {my_integer}")
