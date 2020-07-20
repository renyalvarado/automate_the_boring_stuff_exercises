# ! /usr/bin/env python3
# Coin Toss
import logging
import random

log_format = "%(asctime)s -%(levelname)s -  %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="coin_toss.log", format=log_format)
guess = ""
coin_options = ("tails", "heads")
while guess not in coin_options:
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()
logging.debug(f"guess_01: {guess}")
toss = coin_options[random.randint(0, 1)]  # 0 is tails, 1 is heads
logging.debug(f"toss: {toss}")
if toss == guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    guess = input()
    logging.debug(f"guess_02: {guess}")
    if toss == guess:
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")
