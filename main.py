MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

def report():
    print(f"\nWater: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}\n")

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins (you can use decimals like 1.0, 2.5 etc.).")
    try:
        quarters = float(input("How many quarters ($0.25)? "))
        dimes = float(input("How many dimes ($0.10)? "))
        nickels = float(input("How many nickels ($0.05)? "))
        pennies = float(input("How many pennies ($0.01)? "))
    except ValueError:
        print("⚠️  Invalid input. Please enter numbers only.")
        return -1
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return round(total, 2)

def is_transaction_successful(money_received, drink_cost):
    if money_received == -1:
        print("Payment cancelled due to invalid input.")
        return False
    elif money_received == 0:
        print("You didn't insert any coins.")
        return False
    elif money_received < drink_cost:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    elif money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
    resources["money"] += drink_cost
    return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! ☕\n")

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Coffee machine is shutting down. Goodbye! ☠️")
        break
    elif choice == "report":
        report()
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice. Please type espresso, latte, cappuccino, report or off.")
