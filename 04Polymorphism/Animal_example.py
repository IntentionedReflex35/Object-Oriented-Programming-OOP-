# Parent class
class Animal:
    def __init__(self, name):
        self.name = name.capitalize()

    def speak(self):
        pass              # Children will define their own version.


# Child classes
class Dog(Animal) :
    def speak(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")


class Bird(Animal):
    def speak(self):
        print(f"{self.name} says: Tweet!")


class Cow(Animal):
    def speak(self):
        print(f"{self.name} says: Moo!")


animals = [
    Dog("bruno"),
    Cat("bella"),
    Bird("tweety"),
    Cow("Daisy")
]


# Let's add a new animal
class Lion(Animal):
    def speak(self):
        print(f"{self.name} says: ROAR!")


animals.append(Lion('simba'))

for animal in animals:
    animal.speak()    # same instruction for all animals.
