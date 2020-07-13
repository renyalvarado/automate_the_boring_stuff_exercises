#! /usr/bin/env python3
# English to Pig latin

vowels = ("a", "e", "i", "o", "u", "y")


def maintain_case(old_str, new_str):
    if old_str.istitle():
        return new_str.title()
    elif old_str.isupper():
        return new_str.upper()
    elif old_str.islower():
        return new_str.lower()
    else:
        return new_str


def process_vowel(old_string: str):
    new_string = ""
    final_suffix = "YAY" if word.isupper() and (len(word) > 1) else "yay"
    i = 0
    while i < len(old_string):
        s = old_string[i]
        if s.isalpha():
            new_string += s
        else:
            break
        i += 1
    new_string += final_suffix + old_string[i:]
    return maintain_case(old_string, new_string)


def process_consonant(old_string: str):
    new_string = ""
    cluster = ""
    final_suffix = "AY" if word.isupper() and (len(word) > 1) else "ay"
    i = 0
    while i < len(old_string):
        s = old_string[i]
        if s.lower() not in vowels:
            cluster += s
        else:
            break
        i += 1
    while i < len(old_string):
        s = old_string[i]
        if s.isalpha():
            new_string += s
        else:
            break
        i += 1
    new_string += cluster + final_suffix + old_string[i:]
    return maintain_case(old_string, new_string)


message = input("Enter the English message to translate to Pig Latin: ")

pig_latin = []
words = message.split()
for word in words:
    if word[0].lower() in vowels:
        pig_latin.append(process_vowel(word))
    elif word[0].isalpha():
        pig_latin.append(process_consonant(word))
    else:
        pig_latin.append(word)

print(" ".join(pig_latin))
