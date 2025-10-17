# A simple and fun game of rock, paper, scissors!
import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("Choose rock, paper, or scissors: ")

if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
    print(f"Computer picked: {computer}\nYou win!")
else:
    print(f"Computer picked: {computer}\nComputer wins!")