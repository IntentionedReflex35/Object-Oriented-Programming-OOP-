class Person:
    """Person main class"""
    def __init__(self, name, age, personID):
        self.name = name
        self.age = age
        self.personID = personID

    def display_data(self):
        print(f"Hi, my name is {self.name}. My age is {self.age} and my personID is {self.personID}.")


person0 = Person("lewis", 23, 253)
person1 = Person("Ronaldo", 37, 255)
person2 = Person('Marcelo', 35, 256)

person0.display_data()
person1.display_data()
person2.display_data()

'''
print(person0.name)
print(person0.age)
print(person0.personID)

print(person1.name)
print(person1.age)
print(person1.personID)

print(person2.name)
print(person2.age)
print(person2.personID)'''