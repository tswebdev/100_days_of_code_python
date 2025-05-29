import random
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors!")
items = [r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

""",          
         r"""    
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""", r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

computer_choice = random.choice(items)

if user_choice == "0":
  print("Your choice: ", items[0])
elif user_choice == "1":
  print("Your choice: ", items[1])
elif user_choice == "2":
  print("Your choice: ", items[2])

print("Computer choice: ", computer_choice)

if user_choice not in ["0", "1", "2"]:
  print("You chose an invalid number. You loose!")
elif user_choice == "0" and computer_choice == items[1]:
  print("You loose! Paper wins over Rock")
elif user_choice == "0" and computer_choice == items[2]:
  print("You won! Rock wins over Scissors!")
elif user_choice == "1" and computer_choice == items[0]:
  print("You win! Paper wins over Rock!")
elif user_choice == "1" and computer_choice == items[2]:
  print("You loose! Scissors win over Paper!")
elif user_choice == "2" and computer_choice == items[0]:
  print("You loose! Rock wins over Scissors!")
elif user_choice == "2" and computer_choice == items[1]:
  print("You win! Scissors win over Paper!")
else:
  print("It is a draw! Play again!")