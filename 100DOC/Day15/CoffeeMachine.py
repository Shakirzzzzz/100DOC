def enough_resources(item):
    for key in resources:
        if MENU[item]["ingredients"][key] > resources[key]:
            print(f'Sorry there is not enough {key}')
            return False
        return True
money = 2.5




def serving(item):
    global money
    print('Insert money')
    quarters = (int(input('How many quarters?'))) * 0.25
    dimes = (int(input('How many dimes?'))) * 0.01
    nickles = (int(input('How many nickles'))) * 0.05
    pennies = (int(input('How many pennies?'))) * 0.01

    total_money = quarters + dimes + nickles + pennies
    if total_money < MENU['espresso']['cost']:
        print('Sorry, not enough Money.Refunded the money')
        keep_serving = False
    elif total_money >= MENU[item]['cost']:
        money += MENU[item]['cost']
        return_money = total_money - MENU[item]['cost']
        print(f'Here is your change:${return_money}')
        resources["water"] = resources["water"] - MENU[item]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[item]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[item]["ingredients"]["coffee"]
        print(f'Here is you {item}, Enjoy')







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

keep_serving = True
money = 2.5
while keep_serving == True:
    user_input = input('What would you like? (espresso/latte/cappuccino):')
    if user_input == 'off':
        keep_serving = False
    elif user_input == 'report':
        print(f'water: {resources["water"]}')
        print(f'milk:{resources["milk"]}')
        print(f'coffee:{resources["coffee"]}')
        print(f'Money:${money}')
    elif user_input == 'espresso':

        if  enough_resources('espresso') == False :
            enough_resources('espresso')

        else:
            serving('espresso')
    elif user_input == 'latte':

        if  enough_resources('latte') == False :
            enough_resources('latte')
            keep_serving = False
        else:
            serving('latte')
    elif user_input == 'cappuccino':

        if  enough_resources('cappuccino') == False :
            enough_resources('cappuccino')
            keep_serving = False
        else:
            serving('cappuccino')
    else:
        print('suck my nut and input what you want')









