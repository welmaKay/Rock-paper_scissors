import random
import time

def play_game():
    while True:
        print("\n Welcome to the Wild Treasure Hunt Maze!")
        print("You are in a mysterious maze with **three triangle doors**.")
        print(" Green | Blue | Black")
        
        doors = ["goblins", "three_doors", "treasure"]
        random.shuffle(doors)  
        
        choice = input("\nWhich door do you choose? (green/blue/black): ").strip().lower()
        if choice not in ["green", "blue", "black"]:
            print("Invalid choice! Try again.")
            continue

        result = {"green": doors[0], "blue": doors[1], "black": doors[2]}[choice]
        if result == "goblins":
            print("\nYou enter a dark room filled with **Goblins!**")
            time.sleep(1)
            print("They surround you... GAME OVER!")
        
        elif result == "treasure":
            print("\nYou found a **golden treasure chest!**")
            time.sleep(1)
            treasure_dilemma()
        
        elif result == "three_doors":
            print("\nYou enter a room with **three more doors!**")
            time.sleep(1)
            print("There is a **White Door**, a **Purple Door**, and a **Brown Door**.")
            
            correct_door = random.choice(["white", "purple", "brown"])
            second_choice = input("\nWhich door do you choose? (white/purple/brown): ").strip().lower()

            if second_choice == correct_door:
                print("\n **You found a hidden passage to the treasure room!**")
                time.sleep(1)
                treasure_dilemma()
            else:
                print("\nWrong door! You fall into a pit of spikes... GAME OVER!")

        if not play_again():
            break

def treasure_dilemma():
    print("\n You now have **two choices:**")
    time.sleep(1)
    print("1 Take the treasure and try to escape.")
    print("2 Stay in the treasure room forever...")

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
            print("\n **You found the exit!** You escape with the treasure and live like a king!")
        else:
            print("\n The door leads to a cursed labyrinth... You are **trapped forever!**")
    
    else:
        print("Invalid choice. Try again.")
        return treasure_dilemma()

def play_again():
    response = input("\n Do you want to play again? (yes/no): ").strip().lower()
    return response == "yes"

play_game()