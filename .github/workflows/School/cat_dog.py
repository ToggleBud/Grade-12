class Cat:
    is_animal = True
    animal_type = "felieae"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"my name is {self.name}!")


class Dog:
    is_animal = True
    animal_type = "canidae"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"my name is {self.name}!")

c1 = Cat("Garfield")
c2 = Cat("Prinecess")

d1 = Dog("Clifford")
d2 = Dog("Buddy")

print(c1.is_animal)
print(d1.is_animal)

print(c2.is_animal)
print(d2.is_animal)

print(c1.name)
print(c2.name)
print(d1.name)
print(d2.name)

print(c1.speak())
print(d1.speak())
