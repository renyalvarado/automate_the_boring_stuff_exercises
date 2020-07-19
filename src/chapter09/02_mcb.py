#! /usr/bin/env python3
# Multi Clipboard
"""
Usage: 02_mcb.py save <keyword> - Saves clipboard to keyword.
       02_mcb.py <keyword> - Loads keyword to clipboard.
       02_mcb.py list - Loads all keywords to clipboard.

"""
import sys
import shelve
import pyperclip


def main():
    print("Multi Clipboard")
    count_parameters = len(sys.argv)
    if count_parameters < 2:
        print(__doc__)
        exit()

    with shelve.open('mcb') as mcb_shelf:
        if sys.argv[1].lower() == 'save':
            if count_parameters < 3:
                print("Key is required in order to save clipboard content", file=sys.stderr)
                exit(1)
            mcb_shelf[sys.argv[2]] = pyperclip.paste()
            print("Clipboard content saved in file")
        elif sys.argv[1].lower() == 'list':
            str_keys = str(list(mcb_shelf.keys()))
            pyperclip.copy(str_keys)
            print("Listing keys from file")
            print(str_keys)
        elif sys.argv[1].lower() == 'delete':
            if count_parameters < 3:
                print("Key is required in order to delete content in file", file=sys.stderr)
                exit(1)
            try:
                del mcb_shelf[sys.argv[2]]
                print(f"Key [{sys.argv[2]}] deleted in file")
            except KeyError:
                print(f"Error. Key[{sys.argv[2]}] does not exist in file", file=sys.stderr)
        elif sys.argv[1].lower() == 'delete_all':
            mcb_shelf.clear()
            print("Deleting all keys in file")
        elif sys.argv[1] in mcb_shelf:
            content = mcb_shelf[sys.argv[1]]
            pyperclip.copy(content)
            print(f"Copy content from file. Key[{sys.argv[1]}]")
            print(content)


if __name__ == "__main__":
    main()
