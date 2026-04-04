class Employee:
    # Class constructor
    def __init__(self, name, salary, project):
        self.__name = name
        self.__salary = salary
        self.project = project

    # Show the employee data
    def show_details(self):
        print(f"The name is {self.__name} and salary is {self.__salary}.")

    # Working project
    def work(self):
        print(f"{self.__name} is working on {self.project}.")


# Objects for employee
employee01 = Employee("Marcelo", 90000, 'Video Game')

# Access public name
# print('The value of name is', employee01.__name)
# Call the public methods for details
employee01.show_details()
employee01.work()
