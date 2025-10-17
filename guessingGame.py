# A number guessing game!

import random

number = random.randint(1,100) # Random number between 1 and 100
guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < number:
        print(f"Too low!")
    elif guess > number:
        print(f"Too high!")
    else:
        print(f"You are correct!")