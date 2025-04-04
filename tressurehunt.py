import random #Used to introduce unpredictability and randomness into the game.
import time #

# === Wild Treasure Hunt Maze Game ===
# A text-based adventure game where players explore magical doors
# to find treasure, escape danger, and solve mysterious clues.

# Main game loop
def play_game():
    while True:
        print("\nWelcome to the Wild Treasure Hunt Maze!")
        print("You are in a mysterious maze with **three triangle doors**.")
        print("Green | Blue | Black")

        # Randomly assign contents to the doors each round
        doors = ["goblins", "three_doors", "treasure"]
        random.shuffle(doors)

        # Get the player's first choice
        choice = input("\nWhich door do you choose? (green/blue/black): ").strip().lower()
        if choice not in ["green", "blue", "black"]:
            print("Invalid choice! Try again.")
            continue

        # Determine what's behind the chosen door
        result = {"green": doors[0], "blue": doors[1], "black": doors[2]}[choice]

        # Handle different outcomes based on the room content
        if result == "goblins":
            print("\nYou enter a dark room filled with **Goblins!**")
            time.sleep(1)
            print("They surround you... GAME OVER!")

        elif result == "treasure":
            print("\nYou found a **golden treasure chest!**")
            time.sleep(1)
            clue_room()

        elif result == "three_doors":
            print("\nYou enter a room with **three more doors!**")
            time.sleep(1)
            print("There is a **White Door**, a **Purple Door**, and a **Brown Door**.")

            correct_door = random.choice(["white", "purple", "brown"])
            second_choice = input("\nWhich door do you choose? (white/purple/brown): ").strip().lower()

            if second_choice == correct_door:
                print("\n**You found a hidden passage to a clue room!**")
                time.sleep(1)
                clue_room()
            else:
                print("\nWrong door! You fall into a pit of spikes... GAME OVER!")

        # Ask if the player wants to play another round
        if not play_again():
            break

# Room where a clue is presented to the player
def clue_room():
    print("\nYou enter a mysterious chamber with strange symbols on the walls.")
    time.sleep(1)
    print("In the center, there is a pedestal with a dusty book.")
    print("The book reads: 'Follow the light where shadows dance, beneath the floor lies your chance.'")

    # Choice to investigate further or not
    choice = input("\nDo you investigate the floor? (yes/no): ").strip().lower()
    if choice == "yes":
        print("\nYou push aside a loose tile and find a hidden tunnel!")
        time.sleep(1)
        treasure_dilemma()
    else:
        print("\nYou ignore the clue and wander aimlessly... GAME OVER!")

# Final dilemma room with treasure and escape challenge
def treasure_dilemma():
    print("\nYou now have **two choices:**")
    time.sleep(1)
    print("1. Take the treasure and try to escape.")
    print("2. Stay in the treasure room forever...")

    decision = input("\nWhat do you choose? (escape/stay): ").strip().lower()

    if decision == "stay":
        print("\nThe treasure room locks behind you... You are trapped forever!")
        time.sleep(1)
        print("**GAME OVER!**")
        return

    elif decision == "escape":
        print("\nYou return to the **Green, Blue, and Black** doors.")
        time.sleep(1)
        print("One leads **to freedom**, the others **to doom...**")

        escape_door = random.choice(["green", "blue", "black"])
        final_choice = input("\nWhich door do you take? (green/blue/black): ").strip().lower()

        if final_choice == escape_door:
            print("\n**You found the exit!** You escape with the treasure and live like a king!")
        else:
            print("\nThe door leads to a cursed cave... You are **trapped forever!**")

    else:
        print("Invalid choice. Try again.")
        return treasure_dilemma()

#  wen user wants to replay the game
def play_again():
    response = input("\nDo you want to play again? (yes/no): ").strip().lower()
    return response == "yes"

# Start the adventure
play_game()