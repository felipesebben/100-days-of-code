import random


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
game_images = [rock, paper, scissors]

# Store the user's input.
user_choice = int(input("What do you choose? Type 0 for Rock " +
                  "1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You've typed an invalid number, you lose!")
else:
    if user_choice == 0:
        print(game_images[user_choice])
    elif user_choice == 1:
        print(game_images[user_choice])
    else:
        print(game_images[user_choice])

    # Generate a random choice for the computer.
    computer_choice = random.randint(0, 2)

    if computer_choice == 0:
        print(f"Computer chose:\n{game_images[computer_choice]}")
    elif computer_choice == 1:
        print(f"Computer chose: \n{game_images[computer_choice]}")
    else:
        print(f"Computer chose:\n{game_images[computer_choice]}")

    # Compare choices, determine results, and give feedback to the user.
    if user_choice == computer_choice:
        print("We've got a draw!")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose.")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("You lose.")
