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

#Write your code below this line 👇

import random

#Create a random number between 1-3
random_integer = random.randint (0,2)
print(random_integer)

#Pick 1 random
choice = [rock, paper, scissors]
print(choice[0])

computer_choice = choice[random_integer]
print(computer_choice)

#Question + output
human_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

#Human choice
if human_choice == "0":
  print("You chose " + rock)
elif human_choice == "1":
  print("You chose " + paper)
elif human_choice == "2":
  print("You chose " + scissors)

#Computer choice
print("Computer chose " + computer_choice)

#Result

if human_choice == "0" and computer_choice == rock:
  print ("Its a draw")
elif human_choice == "0" and computer_choice == paper:
  print ("You lose")
elif human_choice == "0" and computer_choice == scissors:
  print ("You Win")

elif human_choice == "1" and computer_choice == rock:
  print ("You Win")
elif human_choice == "1" and computer_choice == paper:
  print ("Its a draw")
elif human_choice == "1" and computer_choice == scissors:
  print ("You lose")

elif human_choice == "2" and computer_choice == rock:
  print ("You lose")
elif human_choice == "2" and computer_choice == paper:
  print ("You Win")
elif human_choice == "2" and computer_choice == scissors:
  print ("Its a draw")