from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self, x):
        print("Inserted value:", x)
    @abstractmethod
    def task(self):
        print('Hi, we are inside Absclass task.')


# test child class
class test_class(Absclass):
    def task(self):
        print('Hi, we are inside test_class task')


# example child class
class example_class(Absclass):
    def task(self):
        print('Hi, we are inside example_class task')


# Objects
test01 = test_class()
test01.task()
test01.print(50)

# Object of example
example01 = example_class()
example01.task()
example01.print(250)

# Testing
print("test_01 is an instance of Absclass:", isinstance(test01, Absclass))
print("example_01 is an instance of Absclass:", isinstance(example01, Absclass))

