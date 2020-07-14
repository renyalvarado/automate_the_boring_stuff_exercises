#! /usr/bin/env python3
# Sandwich Maker

import pyinputplus as pyip

breads = {
    "wheat": 10,
    "white": 20,
    "sourdough": 30
}
print(breads)
bread = pyip.inputMenu(list(breads.keys()))

proteins = {
    "chicken": 30,
    "turkey": 30,
    "ham": 25,
    "tofu": 40
}
print(proteins)
protein = pyip.inputMenu(list(proteins.keys()))

cheeses = {
    "cheddar": 3,
    "Swiss": 8,
    "mozzarella": 2
}
wants_cheese = pyip.inputYesNo(prompt="Do you want cheese? ")
print(cheeses)
cheese_total = 0
if wants_cheese.lower() == "yes":
    cheese = pyip.inputMenu(list(cheeses.keys()))
    cheese_total = cheeses[cheese]

mayonnaise_price = 1.5
wants_mayonnaise = pyip.inputYesNo(prompt=f"Do you want mayonnaise ({mayonnaise_price})? ")
mayonnaise_total = mayonnaise_price if wants_mayonnaise.lower() == "yes" else 0

mustard_price = 2
wants_mustard = pyip.inputYesNo(prompt=f"Do you want mustard ({mustard_price})? ")
mustard_total = mustard_price if wants_mustard.lower() == "yes" else 0

lettuce_price = 1
wants_lettuce = pyip.inputYesNo(prompt=f"Do you want lettuce ({lettuce_price})? ")
lettuce_total = lettuce_price if wants_lettuce.lower() == "yes" else 0

tomato_price = 1
wants_tomato = pyip.inputYesNo(prompt=f"Do you want tomato ({tomato_price})? ")
tomato_total = tomato_price if wants_tomato.lower() == "yes" else 0

sandwiches = pyip.inputInt(prompt="How many sandwiches? ", min=1)

total_per_sandwich = breads[bread] + proteins[protein] + cheese_total \
                     + mayonnaise_total + mustard_total + lettuce_total \
                     + tomato_total
print(f"Total per sandwich: {total_per_sandwich}")
print(f"Total: {sandwiches} x {total_per_sandwich}: {sandwiches * total_per_sandwich}")
