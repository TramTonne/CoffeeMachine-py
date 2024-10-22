from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker=CoffeeMaker()
menu=Menu()
money_machine = MoneyMachine()

cont=True
while cont:
    print('Welcome to Tram coffee machine.')
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order=="off":
        cont=False
    else:
        if order=="report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink=menu.find_drink(order)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


