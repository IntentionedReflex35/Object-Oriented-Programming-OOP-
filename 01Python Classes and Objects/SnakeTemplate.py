# Using Dunder init and instance attributes
class Snake:
    """Snake main blueprint"""
    def __init__(self, name):
        self.name = name

    def modifyName(self, newName):
        self.name = newName


# Objects
snake0 = Snake("python")
snake1 = Snake("Anaconda")

# Printing the values for the two objects
print(snake0.name)
print(snake1.name)
