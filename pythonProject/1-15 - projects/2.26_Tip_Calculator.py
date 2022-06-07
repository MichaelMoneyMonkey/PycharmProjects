#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total = input("What was the total bill?")
tip = input("What percentage tip would you like to give? 10, 12 or 15?")
people = input("How many people to split the bill?")

total_price_with_tip = (float(total) * int(tip)) / 100 + float(total)
indivi_price_int = total_price_with_tip / int(people)

# print (total_price_with_tip)
# print(indivi_price_int)

#round(a_float, 2)

total_price = round(total_price_with_tip, 2)
indivi_price = round(indivi_price_int, 2)

print(f"Eeach person should pay: {indivi_price}")