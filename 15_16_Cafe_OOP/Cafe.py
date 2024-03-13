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

from Snack import Snack
from Robot import Robot
import tools


class CoffeeMachine:
    def __init__(self, water, milk, coffee):
        """Creates a new Coffee Machine"""
        self._keep_working = True
        self._coins = [("quarter", 0.25), ("dime", 0.10), ("nickel", 0.05), ("penny", 0.01)]
        self._supplies = [["water", water], ["milk", milk], ["coffee", coffee]]
        self._money = 0
        self._in_order = ""
        self.bonus_gifts = []

        self.drinks_ordered = 0
        self.money_spent = 0

        self._menu = {
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

    def _report_supplies(self):
        for item in self._supplies:
            print(f"{item[0].title()}: {item[1]}")

    def _add_supplies(self):
        """Replenish water, milk, and coffee supplies"""
        print("Add supplies")
        for item in self._supplies:
            amount_to_add = tools.to_int(input(f"{item[0].title()}: "))
            item[1] += amount_to_add

    def _accept_order(self, order):
        match order:
            case "e":
                self._in_order = "espresso"
                print(f"Espresso: ${self._menu["espresso"]["cost"]}")
            case "l":
                self._in_order = "latte"
                print(f"Latte: ${self._menu["latte"]["cost"]}")
            case "c":
                self._in_order = "cappuccino"
                print(f"Cappuccino: ${self._menu["cappuccino"]["cost"]}")

    def _ask_for_coins(self):
        print("Insert coins")

        for coin in self._coins:
            coins_count = tools.to_int(input(f"{coin[0].title()} (${coin[1]}): "))
            self._money += coin[1] * coins_count

        if self._money >= self._menu[self._in_order]["cost"]:
            print(f"Credit: ${round(self._money, 2)}.")
        else:
            print(f"{self._money} is not enough.")
            self._ask_for_coins()

    def _check_supplies(self):
        missing = []
        for order, supplies in zip(self._menu[self._in_order]["ingredients"], self._supplies):
            if order[1] > supplies[1]:
                missing.append(order[0])
                print(f"Not enough {order[0]}.")

        if len(missing) > 0:
            return False
        else:
            return True

    def _cook(self):
        for order, supplies in zip(self._menu[self._in_order]["ingredients"], self._supplies):
            supplies[1] -= order[1]

        self._money -= self._menu[self._in_order]["cost"]
        self._money = round(self._money, 2)
        self.drinks_ordered += 1
        self.money_spent += self._menu[self._in_order]["cost"]
        print(f"Here's your {self._in_order}! Enjoy!")
        print(f"Credit: ${self._money}")
        self._in_order = ""

    def bonus_gift(self):
        if self.money_spent // 7 > 0:
            num_of_snacks = tools.to_int(self.money_spent // 7)
            for _ in range(0, num_of_snacks):
                self.bonus_gifts.append(Snack("Cookie"))

        if self.money_spent // 15 > 0:
            num_of_toys = tools.to_int(self.money_spent // 15)
            for _ in range(0, num_of_toys):
                self.bonus_gifts.append(Robot("Robot"))

    def work(self):
        while self._keep_working:
            command = input("\nWhat should I do? ")
            match command:
                case "rep":
                    self._report_supplies()
                case "add":
                    self._add_supplies()
                case make if make in {"e", "l", "c"}:
                    self._accept_order(make)
                    while not self._check_supplies():
                        self._add_supplies()
                    if self._money < self._menu[self._in_order]["cost"]:
                        self._ask_for_coins()
                    self._cook()
                case "off":
                    print("Good bye!")
                    self._keep_working = False
                case _:
                    self.work()
