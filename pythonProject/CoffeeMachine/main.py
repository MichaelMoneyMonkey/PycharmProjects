MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# money
money = 0

# machine is on
status = "on"


people = {
    1: {
        'name': 'John',
        'age': '27',
        'sex': 'Male'
    },
    2: {
        'name': 'Marie',
        'age': '22',
        'sex': 'Female'
    }
}

print(MENU["espresso"]["ingredients"]["water"])
print(resources["water"])
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])


while status == "on":

    choice = input("What would you like? (espresso/latte/cappuccino):")

    # turn machine off
    if choice == "off":
        status = "off"

    # ask for resources
    if choice == "report":
        print("Water: " + str(resources["water"]) + "ml")
        print("Milk: " + str(resources["milk"]) + "ml")
        print("Coffee: " + str(resources["coffee"]) + "g")
        print("Money: $" + str(money))

    # check if there are enough resources
    resources_ok = True

    def resources_check():
        global resources_ok
        if MENU[choice]["ingredients"]["water"] < resources["water"]:
            print("There is enough water")
        else:
            print("There is NOT enough water")
            resources_ok = False

        if MENU[choice]["ingredients"]["milk"] < resources["milk"]:
            print("There is enough milk")
        else:
            print("There is NOT enough milk")
            resources_ok = False

        if MENU[choice]["ingredients"]["coffee"] < resources["coffee"]:
            print("There is enough coffee")
        else:
            print("There is NOT enough coffee")
            resources_ok = False

    resources_check()
    print(resources_ok)


    # if there are enough resources user may enter coins
    if resources_ok is True:
        print("You may insert coins")

        # coins
        quarter = float(0.25)
        dime = float(0.10)
        nickle = float(0.05)
        pennie = float(0.01)

        # cost of chosen coffee
        print(choice + " costs $" + str(MENU[choice]["cost"]))

        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickels?"))
        pennies = int(input("How many pennies?"))

        total_coins = quarters * quarter + dimes * dime + nickles * nickle + pennies * pennie
        print("total coin input is " + str(total_coins))

        # check for change or refund
        if total_coins > MENU[choice]["cost"]:
            change_calc = float(total_coins - MENU[choice]["cost"])
            # get 2 decimals
            change = '%.2f' % change_calc
            print("Here is $" + str(change) + " change.")
            print("Here is your " + str(choice) + " ☕. Enjoy!")
            coffee_made = True
        elif total_coins == MENU[choice]["cost"]:
            print("Here is your " + str(choice) + " ☕. Enjoy!")
            coffee_made = True
        elif total_coins < MENU[choice]["cost"]:
            print("You didn't entered enough money. Money refunded")
            coffee_made = False



# TripleM123

    # at end if coffee is made edit resources
    if resources_ok is True and coffee_made is True:
        resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]

