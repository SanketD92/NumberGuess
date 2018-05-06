#!/usr/bin/env python3

import random

number = random.randint(1, 10)
tries = 1

name = input("Hello, What is your username?\n")

print("Hello", name + ".\n", )

Response = input("Would you like to play a game? [Y/N] ")

while (Response !="n") and (Response !="N") and (Response !="y") and (Response !="Y"):
    print("Choose between Y or N only!")
    Response = input("Would you like to play a game? [Y/N] ")
    
if (Response == "n") or (Response=="N"):
    print("Goodbye!")
    exit

if (Response == "y") or (Response=="Y"):
    print("I'm thinking of a number between 1 & 10")

    try:
        guess = int(input("Have a guess: "))
    except ValueError:
        print('Non-numeric data found in the file.')
        guess = int(input("Have a NUMERICAL guess: "))
        
    if guess > number:
        print("Guess lower...")
    if guess < number:
        print("Guess higher..")
    while guess != number:
        tries += 1
        guess = int(input("Try again: "))
        if guess < number:
            print("Guess Higher...")
        if guess > number:
            print("Guess Lower...")
    if guess == number:
        print("You're right! you win! The number was {0} and it only took you {1} tries".format(number, tries))

