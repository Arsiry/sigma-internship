import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalide number. You lose!")
else:
    print(game_images[user_choice])

    compluter_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_images[compluter_choice])

    if user_choice == 0 and compluter_choice == 2:
        print("You win!")
    elif compluter_choice==0 and user_choice==2:
        print("You lose!")
    elif compluter_choice > user_choice:
        print("You lose!")
    elif user_choice > compluter_choice:
        print("You win!")
    elif compluter_choice == user_choice:
        print("It's a draw!")
