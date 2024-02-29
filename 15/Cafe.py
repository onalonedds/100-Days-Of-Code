# Coffee machine

# Hot flavours:
# - Espresso (50ml water, 18g coffee) - $1.50
# - Latte (200ml water, 24g coffee, 150ml milk) - $2.50
# - Cappuccino (250ml water, 24g coffee, 100ml milk) - $3.00

# Resources: water  - 300ml
#            milk   - 200ml
#            coffee - 100g

# Coins: Penny   - 1 cent ($0.01)
#        Nickel  - 5 cents ($0.05)
#        Dime    - 10 cents ($0.10)
#        Quarter - 25 cents ($0.25)

class CoffeeMachine:
    def __init__(self, water, milk, coffee):
        """Creates a new Coffee Machine"""
        self.keep_working = True
        self.supplies = {"water": water, "milk": milk, "coffee": coffee}
        self.money = 0
        self.in_order = ""
        self.menu = {
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
        print("Hello! I'm your new Coffee Machine!")

    def report_supplies(self):
        print(f"Water: {self.supplies["water"]}\n"
              f"Milk: {self.supplies["milk"]}\n"
              f"Coffee: {self.supplies["coffee"]}\n"
              f"Money: ${self.money}")

    def add_supplies(self):
        """Replenish water, milk, and coffee supplies"""
        print("Add supplies")
        water_amount = int(input("Water: "))
        milk_amount = int(input("Milk: "))
        coffee_amount = int(input("Coffee: "))
        self.supplies["water"] += water_amount
        self.supplies["milk"] += milk_amount
        self.supplies["coffee"] += coffee_amount

    def accept_order(self, order):
        match order:
            case "e":
                self.in_order = "espresso"
                print(f"Espresso: ${self.menu["espresso"]["cost"]}")
            case "l":
                self.in_order = "latte"
                print(f"Latte: ${self.menu["latte"]["cost"]}")
            case "c":
                self.in_order = "cappuccino"
                print(f"Cappuccino: ${self.menu["cappuccino"]["cost"]}")

    def ask_for_coins(self):
        print("Insert coins")
        quarter = int(input("Quarter: "))
        dime = int(input("Dime: "))
        nickel = int(input("Nickel: "))
        penny = int(input("Penny: "))
        self.money += round(quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01, 2)
        if self.money >= self.menu[self.in_order]["cost"]:
            print(f"Total: ${round(self.money, 2)}.")
        else:
            print(f"{self.money} is not enough.")
            self.ask_for_coins()

    def check_supplies(self):
        missing = []
        if self.menu[self.in_order]["ingredients"]["water"] > self.supplies["water"]:
            missing.append("water")
            print("Not enough water.")
        if self.menu[self.in_order]["ingredients"]["milk"] > self.supplies["milk"]:
            missing.append("milk")
            print("Not enough milk.")
        if self.menu[self.in_order]["ingredients"]["coffee"] > self.supplies["coffee"]:
            missing.append("coffee")
            print("Not enough coffee.")

        if len(missing) > 0:
            return False
        else:
            return True

    def cook(self):
        self.supplies["water"] -= self.menu[self.in_order]["ingredients"]["water"]
        self.supplies["milk"] -= self.menu[self.in_order]["ingredients"]["milk"]
        self.supplies["coffee"] -= self.menu[self.in_order]["ingredients"]["coffee"]
        self.money -= self.menu[self.in_order]["cost"]
        self.money = round(self.money, 2)
        print(f"Here's your {self.in_order}! Enjoy!")

    def work(self):
        while self.keep_working:
            command = input("\nWhat should I do? ")
            match command:
                case "rep":
                    self.report_supplies()
                case "add":
                    self.add_supplies()
                case make if make in ["e", "l", "c"]:
                    self.accept_order(make)
                    if self.money < self.menu[self.in_order]["cost"]:
                        self.ask_for_coins()
                    while not self.check_supplies():
                        self.add_supplies()
                    self.cook()
                case "off":
                    print("Good bye!")
                    self.keep_working = False
                case _:
                    self.work()
