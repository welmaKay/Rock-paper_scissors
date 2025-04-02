import random

choices = ("rock", "paper", "scissors")

def determine_winner(user, computer_choice):
    if user == computer_choice:
        return "It's a tie!"
    elif (user == "rock" and computer_choice == "scissors") or \
         (user == "scissors" and computer_choice == "paper") or \
         (user == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose, Computer wins!"
def play_game():
    while True:
        user = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower()

        if user == "quit":
            print("Thanks for playing! Goodbye.")
            break
        
        if user not in choices:
            print("Invalid choice, please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"\nYou chose {user}, computer chose {computer_choice}.")
        print(determine_winner(user, computer_choice))
play_game()
