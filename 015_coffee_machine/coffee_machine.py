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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Return True when order can be made, and False when it cannot."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.001
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False when money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f" Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} ☕ .")


# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
machine_is_on = True

while machine_is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

# TODO 2. Turn off the coffee machine by entering "off" to the prompt.
    if choice == 'off':
        machine_is_on = False
# TODO: 3. Print report of all coffee machine resources.
    elif choice == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")


# TODO: 4. Check if resources are sufficient.
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            # TODO: 3. Process coins.
            payment = process_coins()
            # TODO: 4. Check if transaction was successful.
            if is_transaction_successful(payment, drink['cost']):
                # TODO: 5. Make coffee.
                make_coffee(choice, drink['ingredients'])
