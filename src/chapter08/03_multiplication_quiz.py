#! /usr/bin/env python3
# Multiplication Quiz

import random
import time
import pyinputplus as pyip


def create_multipliers(number_of_questions):
    return [(random.randint(0, 9), random.randint(0, 9)) for i in range(number_of_questions)]


multipliers = create_multipliers(10)
print(multipliers)


def create_custom_validator(my_number: int):
    def compare_against_number(my_str):
        try:
            selected_number = int(my_str)
            if selected_number != my_number:
                raise Exception(f"{selected_number} is not the right answer")
        except ValueError:
            raise Exception(f"{my_str} must be a integer")

    return compare_against_number


results = []
for m in multipliers:
    try:
        multiplier01, multiplier02 = m
        prompt = f"{multiplier01} x {multiplier02} = "
        result = multiplier01 * multiplier02
        pyip.inputCustom(create_custom_validator(result), prompt=prompt, timeout=8, limit=3)
        print("Correct\n")
        results.append(True)
        time.sleep(1)
    except pyip.TimeoutException:
        results.append(False)
        print("Out of time!")
    except pyip.RetryLimitException:
        results.append(False)
        print("Out of tries!")

print(f"Total: {['Right' if b else 'Wrong' for b in results]}")
