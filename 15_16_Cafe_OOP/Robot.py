from NiceThing import NiceThing


class Robot(NiceThing):
    def __init__(self, name):
        super().__init__(name, "toy")
        self.message = "I'm AI powered!) Play with me, it's really funny!"

    def action(self):
        super().action()
        print("Sings, dances, tells jokes...")
