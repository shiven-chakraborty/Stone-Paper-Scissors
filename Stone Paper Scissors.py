import random

user_wins = 0
computer_wins = 0
ties = 0

options = ["s", "p", "sc"]
options[0]

while True:
    print()
    user_input = input("Type Stone/Paper/Scissors to choose (S/P/SC respectively), Q to quit the game: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
       print("Please choose a hand to play against the bot")
       continue

    random_number = random.randint(0, 2)
    #stone: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print()
    print("Computer picked", computer_pick + ".")

    if user_input == "s" and computer_pick == "sc":
        user_wins += 1
        print("You won 1 point!")
    elif user_input == "p" and computer_pick == "s":
        user_wins += 1
        print("You won 1 point!")
    elif user_input == "sc" and computer_pick == "p":
        user_wins += 1
        print("You won 1 point!")
    elif user_input == "s" and computer_pick == "s":
        print("It's a tie!")
        ties += 1
    elif user_input == "p" and computer_pick == "p":
        print("It's a tie!")
        ties += 1
    elif user_input == "sc" and computer_pick == "sc":
        print("It's a tie!")
        ties += 1

    else:
        print("You lost")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Whereas you both had", ties, "number of ties")
print("Goodbye!")