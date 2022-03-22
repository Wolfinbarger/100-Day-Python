import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money": 0,
}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_for_off_status(status):
    if status == 'off':
        return False
    return True


def print_report():
    print("Water: " + str(resources["water"]) + 'ml\n' + "Milk: " + str(resources["milk"]) +
          "ml\n" + "Coffee: " + str(resources["coffee"]) + "g\n" + "Money: $" + str(resources["money"]))


coffee_machine_power_status = True

while coffee_machine_power_status is True:

    customer_choice = input(
        "What would you like? (espresso/latte/cappuccino ").lower()

    coffee_machine_power_status = check_for_off_status(customer_choice)

    if customer_choice == 'report':
        clear_screen()
        print_report()
