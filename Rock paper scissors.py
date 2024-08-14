import random

def get_user_choice():
    user_action = input("Enter a choice (rock, paper, scissors): ")
    return user_action.lower()  

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("Happy playing!")
