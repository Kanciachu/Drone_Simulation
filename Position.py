class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        return f"{self.x}, {self.y}, {self.z}"
