from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


game_is_running = True
while game_is_running == True:

    items = menu.get_items()
    choice = input(f'What would you like? ({items})')
    if choice == 'off':
        game_is_running = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        resources = coffee_maker.is_resource_sufficient(drink)
        if resources == True:
            money = money_machine.make_payment(drink.cost)
            if money == True:
                coffee_maker.make_coffee(drink)



