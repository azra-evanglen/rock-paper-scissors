import random

choices = ["rock", "paper", "scissors"]
random_choice = random.choice(choices)
print("computer's choice:", random_choice)

answer = input("what's your choice?").lower()

if answer == random_choice:
    print("draw")

elif answer == "rock" and random_choice == "scissors":
    print("won")

elif answer == "scissors" and random_choice == "paper":
    print("won")

elif answer == "paper" and random_choice == "rock":
    print("won")

else:
    print("lost")
