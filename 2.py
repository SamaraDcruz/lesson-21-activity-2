import random

print("🎮 Rock, Paper, Scissors Game! 🎮")

# Choices
options = ["rock", "paper", "scissors"]

# Computer's choice
computer_choice = random.choice(options)

# User's choice
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

print("Computer chose", computer_choice)

# Check who wins
if user_choice == computer_choice:
    print("It's a tie! 😂😂")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("🎉🎉 You win! 🎉🎉")
else:
    print("Computer wins! 🤖")
