print("Welcome to Rock Paper Scissors!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    player_choice = input("Choose rock (r), paper (p), or scissors (s): ")
    if player_choice not in ["r", "p", "s"]:
        print("Invalid choice, please try again.")
        continue

    import random
    computer_choice = random.choice(["r", "p", "s"])

    if player_choice == "r":
        if computer_choice == "r":
            result = "tie"
        elif computer_choice == "p":
            result = "loss"
        else:
            result = "win"
    elif player_choice == "p":
        if computer_choice == "r":
            result = "win"
        elif computer_choice == "p":
            result = "tie"
        else:
            result = "loss"
    else:
        if computer_choice == "r":
            result = "loss"
        elif computer_choice == "p":
            result = "win"
        else:
            result = "tie"

    print(f"You chose {player_choice}, computer chose {computer_choice}. You {result}!")

    if player_choice == "r" and computer_choice == "r":
        print(rock)
    elif player_choice == "r" and computer_choice == "p":
        print(paper)
    elif player_choice == "r" and computer_choice == "s":
        print(scissors)
    elif player_choice == "p" and computer_choice == "r":
        print(rock)
    elif player_choice == "p" and computer_choice == "p":
        print(paper)
    elif player_choice == "p" and computer_choice == "s":
        print(scissors)
    elif player_choice == "s" and computer_choice == "r":
        print(rock)
    elif player_choice == "s" and computer_choice == "p":
        print(paper)
    else:
        print(scissors)

    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        break

print("Thanks for playing!")
