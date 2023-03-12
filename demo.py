
class CoffeeMachine:
    def __init__(self):
        self.water = 1000
        self.milk = 1000
        self.coffee = 1000
        self.money = 0
        self.menu = {
            "espresso": {"water": 50, "coffee": 18, "cost": 1.5},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3},
        }

    def print_report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: ${self.money}")

    def check_resources(self, drink):
        for item in self.menu[drink]:

            if self.menu[drink][item] > resources(self, item):
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self, drink):
        cost = self.menu[drink]["cost"]
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
        if total < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif total > cost:
            change = round(total - cost, 2)
            print(f"Here is ${change} in change.")
        self.money += cost
        return True

    def make_drink(self, drink):
        for item in self.menu[drink]:
            if item == "cost":
                continue
            setattr(self, item, getattr(self, item) - self.menu[drink][item])
        print(f"Here is your {drink}. Enjoy!")

    def run(self):
        while True:
            choice = input("What would you like? (espresso/latte/cappuccino): ")
            if choice == "off":
                print("Turning off the coffee machine.")
                break
            elif choice == "report":
                self.print_report()
            elif choice in self.menu:
                if self.check_resources(choice):
                    if self.process_coins(choice):
                        self.make_drink(choice)
            else:
                print("Invalid input. Please try again.")
