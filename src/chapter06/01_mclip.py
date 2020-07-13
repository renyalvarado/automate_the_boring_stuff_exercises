#! /usr/bin/env python3
# Multi-clipboard program
import sys
import pyperclip

TEXT = {
    "agree": "Yes, I agree. That sound fine to me",
    "busy": "Sorry, can we do this later this week or next week",
    "upsell": "Would you consider making this a monthly donation?"
}

if len(sys.argv) < 2:
    print("Usage: python3 01_mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyprase = sys.argv[1]
if keyprase in TEXT:
    pyperclip.copy(TEXT[keyprase])
    print(f"Text for {keyprase} copied to clipboard.")
else:
    print(f"There is no text for {keyprase}")
