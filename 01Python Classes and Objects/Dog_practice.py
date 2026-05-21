class Dog:
    def __init__(self, name, age, breed):
        self.name = name.capitalize()
        self.age = age
        self.breed = breed

    def introduce(self):
        print(f"I am {self.name}, a {self.age} year old {self.breed}!")

    def bark(self):
        print(f"{self.name} says: Woof!🐶")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You're now {self.age}")


dog1 = Dog("Scooby", 12, "German Shepherd")
dog1.bark()
dog1.introduce()
dog1.birthday()

print(dog1.name)
