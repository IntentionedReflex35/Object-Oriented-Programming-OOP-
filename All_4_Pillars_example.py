# Let's see how they all connect:
# 🔒 Encapsulation  →  "Protect your data. Control access."
# 👨‍👧 Inheritance   →  "Don't repeat yourself. Share common behaviour."
# 🎭 Polymorphism   →  "Same instruction, each object handles it their own way."
# 🫙 Abstraction    →  "Enforce the contract. Hide the complexity."

# And in one system, they all work together:
from abc import ABC, abstractmethod


# Abstraction 🫙 — enforces the contract
class Animal(ABC):
    def __init__(self, name):
        self.__name = name          # Encapsulation 🔒 — name is protected

    def get_name(self):             # Controlled access to name
        return self.__name

    @abstractmethod
    def speak(self):                # Must be implemented by every child
        pass

    def sleep(self):                # Inheritance 👨‍👧 — shared for free
        print(f"{self.get_name()} is sleeping 💤")


class Dog(Animal):
    def speak(self):                # Polymorphism 🎭 — Dog's own version
        print(f"{self.get_name()} says: Woof! 🐶")


class Cat(Animal):
    def speak(self):                # Polymorphism 🎭 — Cat's own version
        print(f"{self.get_name()} says: Meow! 🐱")


animals = [Dog("Bruno"), Cat("Bella")]

for animal in animals:
    animal.speak()    # Polymorphism at work
    animal.sleep()    # Inherited from Animal
