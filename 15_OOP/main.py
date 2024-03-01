import Cafe

cm = Cafe.CoffeeMachine(5, 500, 5)
cm.work()

print(f"\nDrinks ordered: {cm.drinks_ordered}")
print(f"Money spent: ${cm.money_spent}")
