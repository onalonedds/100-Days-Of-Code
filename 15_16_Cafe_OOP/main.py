import Cafe

cm = Cafe.CoffeeMachine(2000, 2000, 2000)
cm.work()
cm.bonus_gift()

print(f"\nDrinks ordered: {cm.drinks_ordered}")
print(f"Money spent: ${cm.money_spent}")


if len(cm.bonus_gifts) > 0:
    print("We have some gifts for you!")

    for nice_thing in cm.bonus_gifts:
        accept = input(f"Do you want to have a {nice_thing.name}? y/n ")
        if accept == "y":
            nice_thing.is_owned = True

        nice_thing.action()
