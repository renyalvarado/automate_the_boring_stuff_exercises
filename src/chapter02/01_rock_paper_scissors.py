#! /usr/bin/env python3
# Rock, paper, and scissors game
import random
import sys

print("Rock, Paper, Scissors")

wins = 0
losses = 0
ties = 0

long_msg = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}

while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    while True:
        player_move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ")
        if player_move == "q":
            sys.exit()
        if player_move == "r" or player_move == "p" or player_move == "s":
            break
        print("Type one of r, p, s, or q.")

    print(f"{long_msg[player_move]} versus...")

    computer_move = random.choice(list(long_msg.keys()))
    print(f"{long_msg[computer_move]}")

    if player_move == computer_move:
        print("It is a tie!")
        ties = ties + 1
    elif player_move == "r" and computer_move == "s":
        print("You win!")
        wins = wins + 1
    elif player_move == "p" and computer_move == "r":
        print("You win!")
        wins = wins + 1
    elif player_move == "s" and computer_move == "p":
        print("You win!")
        wins = wins + 1
    elif player_move == "r" and computer_move == "p":
        print("You lose!")
        losses = losses + 1
    elif player_move == "p" and computer_move == "s":
        print("You lose!")
        losses = losses + 1
    elif player_move == "s" and computer_move == "r":
        print("You lose!")
        losses = losses + 1
