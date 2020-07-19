#! /usr/bin/env python3
# Random Quiz Generator
import random
import tempfile
from pathlib import Path

print("Random Quiz Generator")

QUIZ_HEADER = """Name:

Date:

Period:

                    State Capitals Quiz (Form 1)

"""

CAPITALS = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

STATES = list(CAPITALS.keys())

BULLETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_bullet(index):
    return BULLETS[index]


def return_random_states(states: list, number_of_states: int = 3) -> list:
    return [(state, CAPITALS[state]) for state in random.sample(states, number_of_states)]


def create_random_options(right_state_number: int) -> tuple:
    state = STATES[right_state_number]
    capital = CAPITALS[state]
    wrong_states = list(STATES)
    del wrong_states[right_state_number]
    question_list = return_random_states(wrong_states)
    answer = (state, capital,)
    question_list.append(answer)
    random.shuffle(question_list)
    return question_list, answer


def create_question(question_number: int, options: list, answer: tuple) -> str:
    right_state, _ = answer
    question = f"{str(question_number).zfill(2)}. What is the capital of {right_state}?"

    options_str = []
    for i, option in enumerate(options):
        _, capital = option
        options_str.append(f"{get_bullet(i)}. {capital}")
    return question + "\n" + "\n".join(options_str)


def create_answer(question_number: int, options: list, answer: tuple) -> str:
    right_state, _ = answer
    index = 0
    for i, option in enumerate(options):
        state, _ = option
        if state == right_state:
            index = i
            break
    return f"{str(question_number).zfill(2)}. {get_bullet(index)}"


def create_single_test(base_directory: Path, prefix, test_number):
    questions_info = [create_random_options(state_number) for state_number in random.sample(range(50), 50)]

    question_filename = base_directory / f"{prefix}quiz{test_number}.txt"
    with open(str(question_filename), mode="w") as fq:
        fq.write(QUIZ_HEADER)
        for i, question_info in enumerate(questions_info):
            fq.write(create_question(i + 1, *question_info) + "\n\n")

    answer_filename = base_directory / f"{prefix}_answers{test_number}.txt"
    with open(str(answer_filename), mode="w") as fa:
        for i, question_info in enumerate(questions_info):
            fa.write(create_answer(i + 1, *question_info) + "\n")


NUMBER_OF_TESTS = 35
for tn in range(NUMBER_OF_TESTS):
    create_single_test(Path(tempfile.gettempdir()), "capitals", tn + 1)
