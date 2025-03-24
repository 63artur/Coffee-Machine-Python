from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
dalej = True
while dalej:
    options = menu.get_items()
    choice = input("What would you like to do? espresso/latte/cappucino ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        dalej = False
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
