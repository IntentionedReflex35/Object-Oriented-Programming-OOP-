# THE FIX
# We create a parent class called Animal that holds everything common to all animals. And then dog, cat and bird just
# say: "I'm an animal - I already have eat and sleep. I just need to add my own unique stuff on top." That is
# INHERITANCE.
# Think of it like genetics. You inherit your eye colour, height and traits from your parents. But you also have your
# unique personality.

# Parent Class (the common blueprint)
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")

    def sleep(self):
        print(f"{self.name} is sleeping ...")

# =================================================
# Child Classes (inherit from Animal - parent class)
# =================================================


class Dog(Animal):             # 👈 Dog inherits Animal. Do not forget to the parent class in brackets of a child class
    def bark(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} says: Meow!")


class Bird(Animal):
    def chirp(self):
        print(f"{self.name} says: Tweet!")
# Without the parenthesis, you are just child the supposed child class like another independent class.

# ==========
# Using them
# ==========


dog01 = Dog("Bruno")
cat01 = Cat("Aline")
bird01 = Bird("Tweety")

# They inherited eat() and sleep() for FREE
dog01.eat()
cat01.sleep()
bird01.eat()

# Plus their own unique behaviours
dog01.bark()
cat01.meow()
bird01.chirp()

# What if a child wants to do things slightly differently? We can override the parent's method.
# Add this method to the Dog child class in addition to the bark function/method.
''' 
def eat(self):
    print(f"{self.name} is wolfing down food at lightning speed.")
'''

# What if the dog want to keep the parent's eating behaviour and add something extra?
'''
class Dog(Animal):
    def eat(self):
        super().eat()  # 👈 first, run Animal's eat()
        print(f"{self.name} then begs for more food!")
'''

# super() lets child reuse parent's method and build on top of it.
