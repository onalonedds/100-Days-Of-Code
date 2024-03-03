from NiceThing import NiceThing


class Snack(NiceThing):
    def __init__(self, name):
        super().__init__(name, "food")
        self.message = "I'm sweet and crunchy) Eat me!"

    def action(self):
        super().action()
        print("Сrunch, crunch...")
