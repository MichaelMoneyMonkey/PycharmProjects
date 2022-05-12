from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

x = "test"
print(x)


# made variable(object) = class MoneyMachine()
money_machine = MoneyMachine()
# object = class CoffeeMaker()
coffee_maker = CoffeeMaker()
menu = Menu()


# object.method
money_machine.report()


is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"Which drink do you want {options}?:")
    print(choice)
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)







