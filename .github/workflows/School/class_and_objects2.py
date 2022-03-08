def q1():
    class Shape:
        def __init__(self, base, height):
            self.base = base
            self.height = height

    class Rectangle(Shape):
        def Area_Finder(self):
            Area = self.base * self.height
            return Area

    class Triangle(Shape):
        def Area_Finder(self):
            Area = self.base * self. height / 2
            return Area

    Rect1 = Rectangle(10, 5)
    Rect1_Area = Rect1.Area_Finder()
    print(f"The area of Rect1 is {Rect1_Area}")

    Tri1 = Triangle(12, 12)
    Tri1_Area = Tri1.Area_Finder()
    print(f"The area of Tri1 is {Tri1_Area}") 

def q2():
    class Animal:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Zebra(Animal):
        def __init__(self, name, age, km_walked, grass_ate):
            super().__init__(name, age)
            self.km_walked = km_walked
            self.grass_ate = grass_ate
        def details(self):
            print(f"{self.name} is {self.age} years old")
            print(f"{self.name} the Zebra walked {self.km_walked}km and ate {self.grass_ate} grass slices")

    class Dolphin(Animal):
        def __init__(self, name, age, km_swam, fish_ate):
            super().__init__(name, age)
            self.km_swam = km_swam
            self.fish_ate = fish_ate
        def details(self):
            print(f"{self.name} is {self.age} years old")
            print(f"{self.name} the Dolphin swam {self.km_swam}km and ate {self.fish_ate} fish")

    z1 = Zebra("Marty", 6, 26, 122)
    z1.details()
    z2 = Zebra("Marty the 2nd", 8, 28, 124)
    z2.details()

    d1 = Dolphin("Beluga", 4, 16, 22)
    d1.details()
    d2 = Dolphin("Crab", 8, 18, 24)
    d2.details()

q2()

class Automobile:
    def __init__(self, brand, year, name):
        self.brand = brand
        self.year = year
        self.name = name
    def lonely():
        print("I'm just a class!")

class Car(Automobile):
    pass
class Sedan(Car):
    pass
class Sport(Car):
    pass
class Truck(Automobile):
    pass
class Van(Automobile):
    pass