#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


import random
#logo
from art import logo
from art import logo2

print(logo)
print(logo2)

#generate list 1-100
range_100 = range(1, 100)
list_100 = list(range_100)
print(list_100)
#generate number between 1-100
random_nr = random.choice(list_100)
print(f"The random number is {random_nr}")

#choose difficulty
difficulty = input('Choose a difficulty. Type "easy" or "hard":')

if difficulty == "easy":
  tries = 10
elif difficulty == "hard":
  tries = 5
else:
  print('You didn\'t typed "easy" or "hard". Try again')

#loop tries
while tries > 0:
  print(f"You have {tries} tries remaining.")
  guess = input("Guess a number:")


  if int(guess) > int(random_nr):
    print("Too high.")
  elif int(guess) < int(random_nr):
    print("Too low.")
  elif int(guess) == int(random_nr):
    print("You guessed correctly! You win!")
    #to stop game
    tries = 0

  tries -= 1

  if tries == 0:
    print(f"Sorry you lost. The number we were looking for was {random_nr}")