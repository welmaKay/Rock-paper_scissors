ef determine_winner(user, computer_choice):
    if user == computer_choice:
        return "It's a tie!"
    elif (user == "rock" and computer_choice == "scissors") or \
         (user == "scissors" and computer_choice == "paper") or \
         (user == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose, Computer wins!