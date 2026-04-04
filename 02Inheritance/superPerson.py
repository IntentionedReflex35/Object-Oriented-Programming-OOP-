# Person Parent Class
class Person:
    def person_data(self, name, age):
        print("Hello from the Person CLass")
        print(f"My name is {name} and I'm {age} years old.")


# Company Parent Class
class Company:
    def company_data(self, comp_name, location):
        print("Welcome to the Company!")
        print(f"The company name is {comp_name}. It is located at {location}")


# Employee child class
class Employee(Person, Company):
    def employee_data(self, salary, skill):
        print(f"Welcome to the Employee class")
        print(f"Salary is {salary}. Skill: {skill}")


# Objects for employee
emp01 = Employee()

# Get data on screen
emp01.person_data('Marcelo', 33)
emp01.company_data('Real Madrid', 'Madrid')
emp01.employee_data('$98570000', 'Data Science')
