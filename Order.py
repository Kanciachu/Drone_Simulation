class Order():
    def __init__(self, destination, load=None, type_="DELIVERY"):
        self.type = type_
        self.destination = destination
        self.load = load

    def get_order(self):
        return self.type, self.destination, self.load

    def display_order(self):
        print(f"{self.type.upper()} : DESTINATION: {self.destination.display()} | LOAD : {self.load}")