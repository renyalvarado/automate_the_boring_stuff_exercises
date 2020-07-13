#! /usr/bin/env python3
# Fortune teller
import random

print("Magic 08 ball")


def get_answer(answer_number):
    if answer_number == 1:
        return "It is certain"
    elif answer_number == 2:
        return "It is decidedly so"
    elif answer_number == 3:
        return "Yes"
    elif answer_number == 4:
        return "Reply hazy try again"
    elif answer_number == 5:
        return "Ask again later"
    elif answer_number == 6:
        return "Concentrate and ask again"
    elif answer_number == 7:
        return "My reply is no"
    elif answer_number == 8:
        return "Outlook not so good"
    elif answer_number == 9:
        return "Very doubtful"


def answer_smaller():
    messages = [
        "It is certain",
        "It is decidedly so",
        "Yes",
        "Reply hazy try again",
        "Ask again later",
        "Concentrate and ask again",
        "My reply is no",
        "Outlook not so good",
        "Very doubtful"
    ]
    return random.choice(messages)


r = random.randint(1, 9)
fortune = get_answer(r)
print(f"Using get_answer: {fortune}")
print(f"Using answer_smaller: {answer_smaller()}")
