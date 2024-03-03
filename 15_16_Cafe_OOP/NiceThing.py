class NiceThing:
    def __init__(self, name, kind):
        self.name = name
        self.type = kind
        self.message = ""
        self.is_owned = False

    def action(self):
        if self.is_owned:
            print(f"{self.message}")
        else:
            print("Why don't you want me?.. :(")
