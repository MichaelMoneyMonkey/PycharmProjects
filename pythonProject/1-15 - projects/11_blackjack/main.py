############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.




from art import logo 
import random

print(logo)


#card list
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
print ("Possible card output : " + str(cards))

# testers
# human_num1 = 11
# human_num2 = 3
# pc_num1 = 11
# pc_num2 = 5


human_num1 = random.choice(cards)
human_num2 = random.choice(cards)
pc_num1 = random.choice(cards)
pc_num2 = random.choice(cards)
  

print ("First card : " + str(human_num1))
print ("Second card : " + str(human_num2))


human_total = human_num1 + human_num2
pc_total = pc_num1 + pc_num2

#check for blackjack

if human_total == 21:
  print("You have blackjack! You Win!")
elif pc_total == 21:
  print("Computer has blackjack! You lose.")
elif human_total == 21 and pc_total == 21:
  print("Both you and the computer have blackjack. It's a Push.")
else: 
  print (f"You have {human_num1 + human_num2}")
  print ("Computer got : " + str(pc_num1))


  #ace check human
  if human_num1 == 11 or human_num2 == 11:
    human_has_ace = True
    print("human has ace")
  else:
    human_has_ace = False
    print("human has no ace")
  #double ace check human
  if human_num1 == 11 and human_num2 == 11:
    human_total = 12
    human_has_ace = True

    
  #ace check pc
  if pc_num1 == 11 or pc_num2 == 11:
    pc_has_ace = True
  else:
    pc_has_ace = False
  #double ace check pc
  if pc_num1 == 11 and pc_num2 == 11:
    pc_total = 12
    pc_has_ace = True



##### DRAW CARDS FOR HUMAN

    
  #ask to draw card
  another_card = input('Do you want another card? Type "y" or "n"')


  
  #draw cards for humans WITH ace
  while another_card == "y" and human_has_ace == True:
    human_num3 = random.choice(cards)
    human_total = human_total + human_num3
    print(human_total)
    if human_num3 == 11 and human_total > 21 and human_total != 31:
      human_total = human_total - 10
    if human_num3 == 11 and human_total == 31:
      human_total = human_total - 10
      human_has_ace = False
    
    if human_total < 21:
      print(f"You drew a {human_num3}, your total score is now: {human_total}")
      another_card = input('Do you want another card? Type "y" or "n"')
    elif human_total == 21:
      print("You have blackjack!")
    elif human_total > 21:
      human_total = human_total - 10
      human_has_ace = False
      #If human_has_ace becomes false this means the 11 became a 1 and we switch to the next while loop
      print(f"You drew a {human_num3}, your total score is now: {human_total}")
      another_card = input('Do you want another card? Type "y" or "n"')
      
      if another_card == "n":
        print("your final score is: " + str(human_total))
    
    
  #draw cards for humans WITHOUT ace or who "lost" ace(11 became 1)
  while human_total < 21 and another_card == "y" and human_has_ace == False:
    human_num3 = random.choice(cards)
    human_total = human_total + human_num3
      
    print(f"You drew a {human_num3}, your total score is now: {human_total}")
      
    if human_total == 21:
      print("You have blackjack!")
    elif human_total > 21:
      print(f"You score is {human_total} this is over 21 you can't draw anymore.")
    elif human_total < 21:
      another_card = input('Do you want another card? Type "y" or "n"')
      if another_card == "n":
        if human_total > 21:
          print(f"You score is {human_total} this is over 21 you can't draw anymore.")
        else:
          print("your final score is: " + str(human_total))



        

  ######### DRAW CARDS FOR PC
  print(f"check up pc n1: {pc_num1} n2: {pc_num2} total: {pc_total}")
  #pc has ace     
  while pc_total < 17 and pc_has_ace == True:
    pc_num3 = random.choice(cards)
    pc_total = pc_total + pc_num3

    if pc_num3 == 11 and pc_total > 21:
      pc_total = pc_total - 10

    if pc_total > 21:
      pc_total = pc_total - 10
      pc_has_ace = False
    
    
    print(f"The computer drew a {pc_num3} and has now {pc_total}")
    
    
    

    

  #pc has no ace or "lost" ace
  while pc_total < 17 and pc_has_ace == False:
    pc_num3 = random.choice(cards)
    pc_total = pc_total + pc_num3
    print(f"The computer drew a {pc_num3} and has now {pc_total}")
    if pc_total == 21: 
      print("The computer has blackjack")
    elif pc_total > 21:
      print(f"The computer has {pc_total}, this is over 21")

  if pc_total >= 17 and pc_total < 21:
    print(f"The computer has {pc_total}")


  print(f"\nYou have {human_total}")
  print(f"Computer has {pc_total}\n")

  #test
  # human_total = 28
  # print(f"test human total {human_total}")
  # pc_total = 17
  # print(f"test pc total {pc_total}")

  if human_total > 21 and pc_total > 21:
    print(f"It's a push / draw")
  elif human_total < 21 and pc_total > 21: 
    print("You win")
  elif human_total > 21 and pc_total < 21: 
    print("You lose")
  elif  human_total > pc_total:
    print("You win")
  elif human_total == pc_total:
    print("It's a push / draw")
  else:
    print("You lose")