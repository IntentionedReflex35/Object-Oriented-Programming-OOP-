# Parent Class
class Vehicle:
    def Vehicle_data(self):
        print("Hello from the vehicle class")


# Car Child Class
class Car(Vehicle):
    def Car_Data(self):
        print("Hello from the car class")


# Bike Child Class
class Bike(Vehicle):
    def Bike_Data(self):
        print("Hello from Bike")


# Objects based on car
car01 = Car()
bike01 = Bike()

# Get vehicle data
car01.Vehicle_data()
car01.Car_Data()

print('=================')

bike01.Vehicle_data()
bike01.Bike_Data()

