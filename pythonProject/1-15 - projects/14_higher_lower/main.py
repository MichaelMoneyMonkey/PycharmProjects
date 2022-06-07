from art import logo, vs
from game_data import data
import random

print(logo)
# print(data)

# https://www.checkli.com/checklists/view/626a9c3868312

option_a = random.choice(data)
option_b = random.choice(data)
print(option_a)
print(option_b)
print("\n\n\n\n\n")



# print("Compare A: " + option_a['name'] + ", a " + option_a['description'] + ", from " + option_a['country'])

#compare A
print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
#vs logo
print(vs)
#compare B
print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

#ask for answer
answer = input('\n\n Who has the most followers? Type "a" or "b"')
print(f"answer is {answer}")

#check if answer is right
if option_a['follower_count'] > option_b['follower_count']:
  most_followers = "a"
else: 
  most_followers = "b"

print(f"most_followers is {most_followers}")

if most_followers == answer:
  result = "You are right"
else:
  result ="You were wrong"

print(result)

#generate score
score = 0
if result == "You are right":
  score += 1

print(f"score is {score}")

# while result == "You are right":
#   answer = input('\n\n Who has the most followers? Type "a" or "b"')
# print(f"answer is {answer}")







# dict = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cristiano Ronaldo',
#         'follower_count': 215,
#         'description': 'Footballer',
#         'country': 'Portugal'
#     }
# ]


# print(dict[0])