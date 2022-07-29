class Order:
    def __init__(self, destination, load=None, type_="DELIVERY"):
        self.type = type_
        self.destination = destination
        self.load = load

    def get_order(self):
        return self.type, self.destination, self.load

    def display_order(self):
        return f"{self.type.upper()} : DESTINATION0: {self.destination.display()} | LOAD : {self.load}"
