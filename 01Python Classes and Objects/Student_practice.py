class Student:
    def __init__(self, name, age, gender, programme, height, weight):
        self.name = name
        self.age = age
        self.gender = gender.capitalize()
        self.programme = programme
        self.weight = weight
        self.height = height

    def introduction(self):
        message = f"I am {self.name}, a {self.age} year old {self.gender} pursuing a degree in {self.programme}."
        print(message)

    def metrics(self):
        print(f"Your metrics are {self.height}cm in height and {self.weight}kg in weight.")


student1 = Student("Alice", 19, "female", "Computer Engineering", 72, 162)
student1.introduction()
student1.metrics()
