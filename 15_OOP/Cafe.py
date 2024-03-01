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

import tools


class CoffeeMachine:
    def __init__(self, water, milk, coffee):
        """Creates a new Coffee Machine"""
        self.keep_working = True
        self.coins = [("quarter", 0.25), ("dime", 0.10), ("nickel", 0.05), ("penny", 0.01)]
        self.supplies = [["water", water], ["milk", milk], ["coffee", coffee]]
        self.money = 0
        self.in_order = ""
        self.menu = {
            "espresso": {
                "ingredients":
                    [
                        ["water", 50],
                        ["coffee", 18]
                    ]
                ,
                "cost": 1.5
            },
            "latte": {
                "ingredients":
                    [
                        ["water", 200],
                        ["milk", 150],
                        ["coffee", 24]
                    ]
                ,
                "cost": 2.5
            },
            "cappuccino": {
                "ingredients":
                    [
                        ["water", 200],
                        ["milk", 150],
                        ["coffee", 24]
                    ]
                ,
                "cost": 3.0
            }
        }
        print("Hello! I'm your new Coffee Machine!")
        print("Commands: 'rep' for report, 'add' for adding supplies, 'e, l, or c' for Espresso, Latte, or Cappuccino.")

    def report_supplies(self):
        for item in self.supplies:
            print(f"{item[0].title()}: {item[1]}")

    def add_supplies(self):
        """Replenish water, milk, and coffee supplies"""
        print("Add supplies")
        for item in self.supplies:
            amount_to_add = tools.to_int(input(f"{item[0].title()}: "))
            item[1] += amount_to_add

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

        for coin in self.coins:
            coins_count = tools.to_int(input(f"{coin[0].title()} (${coin[1]}): "))
            self.money += coin[1] * coins_count

        if self.money >= self.menu[self.in_order]["cost"]:
            print(f"Credit: ${round(self.money, 2)}.")
        else:
            print(f"{self.money} is not enough.")
            self.ask_for_coins()

    def check_supplies(self):
        missing = []
        for order, supplies in zip(self.menu[self.in_order]["ingredients"], self.supplies):
            if order[1] > supplies[1]:
                missing.append(order[0])
                print(f"Not enough {order[0]}.")

        if len(missing) > 0:
            return False
        else:
            return True

    def cook(self):
        for order, supplies in zip(self.menu[self.in_order]["ingredients"], self.supplies):
            supplies[1] -= order[1]

        self.money -= self.menu[self.in_order]["cost"]
        self.money = round(self.money, 2)
        print(f"Here's your {self.in_order}! Enjoy!")
        print(f"Credit: ${self.money}")
        self.in_order = ""

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
                    while not self.check_supplies():
                        self.add_supplies()
                    if self.money < self.menu[self.in_order]["cost"]:
                        self.ask_for_coins()
                    self.cook()
                case "off":
                    print("Good bye!")
                    self.keep_working = False
                case _:
                    self.work()
