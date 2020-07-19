#! /usr/bin/env python3
# Mad Libs
import re

print("Mad Libs")

text = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events"
re_key_words = re.compile("ADJECTIVE|NOUN|ADVERB|VERB")

print("Original text")
print(text + "\n")

answers = []
vowels = "aeiou"
for my_match in re_key_words.findall(text):
    article = "an" if my_match[0].lower() in vowels else "a"
    new_element = input(f"Enter {article} {my_match.lower()}: ")
    answers.append(new_element)

print("\nNew text")
new_text = re.sub(re_key_words, lambda x: answers.pop(0), text)
print(new_text)
with open("new_text.txt", "w") as f:
    f.write(new_text + "\n")
