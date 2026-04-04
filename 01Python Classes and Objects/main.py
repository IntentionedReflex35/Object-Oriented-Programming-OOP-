class Snake:
    """Snake main blueprint"""
    name = "Anaconda"

    # Method to change name attribute
    def modifyName(self, new_name):
        self.name = new_name


# Objects based on snake. The below line is an object- a variable outside the class
snake01 = Snake()

print(snake01.name)

# Modify the name  using modifyNames
snake01.modifyName('Python')
print(snake01.name)
