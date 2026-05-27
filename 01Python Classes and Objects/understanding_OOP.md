# The Beginning

---

### Writing code before OOP

Imagine you're building a system to manage students in a school. You start writing code like this:

```python
student1_name = "Ali"
student1_age = 20
student1_grade = "A"

student2_name = "Sara"
student2_age = 22
student2_grade = "B"
```

Fine...that works for 2 students. What about 500 students?

You'd have 1500 variables flying around. And if you want to say, print every student's info — you'd have to manually write it for each one.

**The problem here**
> The data is just floating loosely. Nothing is grouping related things together.

**The root cause**
> We have no way to bundle related data (and actions on that data) together into one neat package.

**The fix**

What if we could create a blueprint — like a template — that says:
> "Every student has a name, an age and a grade."

And then from that blueprint, we just stamp out as many students as we need?

That's exactly what OOP gives us. 🎯

---

### Enter: Classes and Objects
Think of it like this:
> A **Class** is like an architectural blueprint of a house. A **blueprint** tells you: every house will have a door, windows, a kitchen. But the blueprint itself is not the house.

> An **Object** is the actual house built from that blueprint. You can build 100 different houses from the same blueprint — each with its own colour, address, and owner.


In Python:
```python
# THE BLUEPRINT
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
# Stamping out actual OBJECTS from the blueprint
student1 = Student("Ali", 20, "A")
student2 = Student("Sara", 22, "B")
    
print(student1.name)
print(student2.grade)
```
Clean🧹

---

### What is `__init__` and `self`?

`__init__` is just the "set up" function. When you create a new student, Python automatically runs `__init__` to fill in all the details. Think of it as the moment a new student fills out their **enrollment form**.

`self` just means "this specific object." When `student1` is created, `self` refers to `student1`. Same applies to when `student2` is created. It is how each object keeps track of its own data.

---

**What if students could also do things — like introduce themselves?**

Without OOP, you'd write a separate function:
```python
def introduce(name, age):
        print(f"Hi, I'm {name} and I'm {age} years old.")
        
introduce(student1_name, student1_age)
```

This works, but again, that function is just floating around, not connected to the student at all.

**What if the student could just... introduce themselves?**
```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def introduce(self):  # This is called a METHOD.
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")
    
student1 = Student("Ali", 20, "A")
student1.introduce()
```

> Functions that live inside a class are called **methods**. They belong to the object, just like the data does.

---

### The 4 Pillars of OOP

This is just the foundation — Classes & Objects. OOP has 4 big ideas built on top of this:

- Encapsulation — hide messy internal details
- Inheritance — one class can inherit from another
- Polymorphism — same action, different behaviour depending on the object
- Abstraction — show only what's necessary, hide what is not
