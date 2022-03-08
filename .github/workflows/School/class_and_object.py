def q1():
    class Fruit:
        def __init__(self, name, colour, size):
            self.name = name
            self.colour = colour
            self.size = size
            

    f1 = Fruit("Strawberry", "Red", "Small")

    print(f1.name)
    print(f1.colour)
    print(f1.size)

class inventory:
    def __init__(self, item, price):
        self.item = item
        self.price = price
item1 = inventory("Book")