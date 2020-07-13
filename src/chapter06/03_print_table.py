#! /usr/bin/env python3
# Table Printer

table_data = [["apples", "oranges", "cherries", "banana"],
              ["Alice", "Bob", "Carol", "David"],
              ["dogs", "cats", "moose", "goose"]]

max_columns = max([len(x) for x in table_data])
max_sizes = [max([0 if i > (len(x) - 1) else len(x[i]) for x in table_data]) for i in range(max_columns)]
print(max_sizes)

print("Using For")
for row in table_data:
    for i in range(max_columns):
        my_string = "" if i > (len(row) - 1) else row[i]
        print(my_string.rjust(max_sizes[i]) + " ", end="")
    print()
print()

print("Using comprehension")
for row in table_data:
    print("".join([("" if i > (len(row) - 1) else row[i]).rjust(max_sizes[i]) + " " for i in range(max_columns)]))
print()
