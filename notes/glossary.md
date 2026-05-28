# 📘 OOP Glossary — Plain Language Reference

> *Every term you will encounter in Object-Oriented Programming, explained the way a person explains it — not the way a textbook does.*

---

## How to Use This Glossary

This is not a dictionary. It is a **mental model builder**.

Each entry follows the same structure:

- **Plain definition** — what it actually means
- **The intuition** — an analogy or real-world framing
- **In Python** — a minimal code example
- **Common misconception** — the thing most beginners get wrong (where relevant)

Terms are grouped by concept, not listed alphabetically, because understanding flows better when related ideas sit next to each other.

---

## 🏗️ Foundational Concepts

---

### Object

**What it is:**
A self-contained unit that bundles together *data* (what it knows) and *behaviour* (what it can do).

**The intuition:**
Think of a car. A car has attributes — colour, fuel level, current speed. And it has behaviours — accelerate, brake, honk. An object in Python works the same way: it holds its own data and comes with actions built in.

**In Python:**
```python
my_car = Car(colour="red", fuel=100)
my_car.accelerate()  # calling a behaviour
print(my_car.fuel)   # accessing data
```

---

### Class

**What it is:**
A blueprint or template that defines what objects of a certain type look like and can do. The class is not the object — it is the *instructions for creating* objects.

**The intuition:**
An architect's floor plan is not a house. But every house built from that plan shares the same structure. A class is the floor plan. Each object you create from it is a house.

**In Python:**
```python
class Car:
    def __init__(self, colour, fuel):
        self.colour = colour
        self.fuel = fuel

# The class is Car. The object is my_car.
my_car = Car(colour="red", fuel=100)
```

**Common misconception:**
Beginners often confuse the class with the object. Remember — `Car` is the blueprint. `my_car` is the actual thing built from it.

---

### Instance

**What it is:**
A specific object created from a class. Every time you call a class like a function, you create a new instance.

**The intuition:**
If `Car` is the blueprint, then `my_car`, `your_car`, and `taxi` are all instances — each is a separate car built from the same plan, each with its own fuel level and colour.

**In Python:**
```python
my_car = Car("red", 100)    # instance 1
your_car = Car("blue", 80)  # instance 2

# They are independent — changing one does not affect the other
```

---

### Instantiation

**What it is:**
The act of creating an instance from a class. When you call `Car(...)`, that process of creation is called instantiation.

**The intuition:**
Stamping a cookie from a cookie cutter. The cutter is the class. The cookie is the instance. Stamping is instantiation.

---

### Attribute

**What it is:**
A variable that belongs to an object or class. It stores data about that thing.

**The intuition:**
A person's attributes might be their name, age, and height. These are facts *about* the person that travel with them.

**In Python:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name   # attribute
        self.age = age     # attribute
```

> See also: **Instance Attribute**, **Class Attribute**

---

### Instance Attribute

**What it is:**
An attribute that belongs to a specific instance. Each object has its own copy.

**The intuition:**
Your bank account balance is an instance attribute. It belongs to *you*, not to all bank customers. Someone else's balance is stored separately.

**In Python:**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner     # unique to each instance
        self.balance = balance # unique to each instance
```

---

### Class Attribute

**What it is:**
An attribute that belongs to the class itself and is shared by every instance of that class.

**The intuition:**
The interest rate at a bank applies to all accounts equally. It is not stored on each account individually — it belongs to the bank (the class). If it changes, it changes for everyone.

**In Python:**
```python
class BankAccount:
    interest_rate = 0.05  # class attribute — shared by all instances

    def __init__(self, owner, balance):
        self.owner = owner     # instance attribute
        self.balance = balance # instance attribute
```

**Common misconception:**
If you assign a class attribute to a specific instance (`my_account.interest_rate = 0.07`), you create a new *instance attribute* that shadows the class attribute. The class attribute is unchanged. This catches many beginners off guard.

---

### Method

**What it is:**
A function defined inside a class. It describes what an object *can do*.

**The intuition:**
If attributes are nouns (what an object *is*), methods are verbs (what an object *does*). A `Dog` class might have attributes like `name` and `breed`, and methods like `bark()` and `fetch()`.

**In Python:**
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):          # this is a method
        print(f"{self.name} says: Woof!")
```

---

### `self`

**What it is:**
A reference to the current instance of the class. It is how a method knows *which object* it is operating on.

**The intuition:**
Imagine you are in a room full of people and someone says "raise your own hand." The word "own" tells each person to raise *their* hand, not anyone else's. `self` is that word — it tells the method to operate on *this* specific object.

**In Python:**
```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1  # self.count refers to THIS object's count
```

**Common misconception:**
`self` is not a keyword — it is a convention. You could name it anything. But you should always name it `self`. Deviating from this confuses everyone (including future you).

---

### Constructor (`__init__`)

**What it is:**
A special method that runs automatically when a new object is created. Its job is to set up the object's initial state.

**The intuition:**
When a new employee joins a company, HR runs through an onboarding checklist — assign a desk, create a login, issue a badge. The constructor is that onboarding checklist: it sets everything up the moment the object comes into existence.

**In Python:**
```python
class Employee:
    def __init__(self, name, department):  # runs automatically on creation
        self.name = name
        self.department = department
        self.active = True  # default setup
```

---

## 🔒 The Four Pillars

---

### Encapsulation

**What it is:**
The practice of bundling data and the methods that work on that data together inside a class, and controlling what the outside world can access.

**The intuition:**
A TV remote has buttons on the outside and complex circuitry on the inside. You interact with the buttons — you do not need to understand the circuit board to change the channel. Encapsulation is that separation: a clean interface on the outside, protected internals on the inside.

**In Python:**
```python
class Thermostat:
    def __init__(self, temperature):
        self._temperature = temperature  # protected — don't access directly

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if 10 <= value <= 30:            # validation happens here
            self._temperature = value
        else:
            raise ValueError("Temperature out of safe range.")
```

---

### Inheritance

**What it is:**
A mechanism that allows a new class to take on the attributes and methods of an existing class, then add or change what it needs.

**The intuition:**
A `SavingsAccount` *is a* `BankAccount`. It has everything a bank account has, plus a few savings-specific features. Rather than writing `BankAccount` from scratch again, inheritance lets `SavingsAccount` say: "Start with everything a `BankAccount` already does, then I'll add my own bits."

**In Python:**
```python
class BankAccount:               # parent (base) class
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

class SavingsAccount(BankAccount):  # child class — inherits from BankAccount
    def __init__(self, balance, interest_rate):
        super().__init__(balance)   # call parent's constructor
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)
```

> See also: **Parent Class**, **Child Class**, **`super()`**

---

### Polymorphism

**What it is:**
The ability of different objects to respond to the same method call in their own way. Same interface, different behaviour.

**The intuition:**
The instruction "speak" means something different depending on who you give it to. A dog barks. A cat meows. A person says hello. Same instruction — different responses. That is polymorphism.

**In Python:**
```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Parrot:
    def speak(self):
        return "Polly wants a cracker!"

animals = [Dog(), Cat(), Parrot()]

for animal in animals:
    print(animal.speak())  # each responds differently to the same call
```

---

### Abstraction

**What it is:**
Hiding complex implementation details and exposing only what is necessary. Letting users interact with a simplified interface without needing to understand what is happening underneath.

**The intuition:**
You drive a car without understanding how the engine works. The steering wheel, pedals, and gear stick are an abstraction layer over tremendous mechanical complexity. Abstraction in code does the same thing — it gives you a simple interface over complex logic.

**In Python:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):             # abstract class — cannot be instantiated directly
    @abstractmethod
    def area(self):           # abstract method — subclasses MUST implement this
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):           # concrete implementation
        return 3.14159 * self.radius ** 2
```

---

## 🧬 Inheritance Deep Dive

---

### Parent Class (Base Class / Superclass)

**What it is:**
The class being inherited from. It provides the foundation that child classes build upon.

**Alternative names:** Base class, superclass — all mean the same thing.

---

### Child Class (Derived Class / Subclass)

**What it is:**
A class that inherits from a parent class. It gets all the parent's attributes and methods automatically, and can add new ones or override existing ones.

**Alternative names:** Derived class, subclass — all mean the same thing.

---

### `super()`

**What it is:**
A built-in function that gives you access to the parent class's methods from inside a child class. Most commonly used to call the parent's `__init__`.

**The intuition:**
When a child class adds its own `__init__`, it replaces the parent's setup entirely — unless you explicitly call `super()`. Think of it as saying: "Do everything the parent normally does first, then let me add my own stuff."

**In Python:**
```python
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class ElectricCar(Vehicle):
    def __init__(self, speed, battery_capacity):
        super().__init__(speed)               # run parent's __init__ first
        self.battery_capacity = battery_capacity  # then add our own attribute
```

---

### Method Overriding

**What it is:**
When a child class provides its own implementation of a method that already exists in the parent class, replacing the parent's version for that child.

**The intuition:**
The parent class `Animal` has a `speak()` method that returns `"..."`. The `Dog` child class overrides it to return `"Woof!"`. The dog *overrides* the generic behaviour with its own specific version.

---

### Multiple Inheritance

**What it is:**
When a class inherits from more than one parent class at the same time.

**In Python:**
```python
class Flyable:
    def fly(self):
        return "I can fly"

class Swimmable:
    def swim(self):
        return "I can swim"

class Duck(Flyable, Swimmable):  # inherits from both
    pass
```

**Common misconception:**
Multiple inheritance can cause the **diamond problem** — ambiguity about which parent's method to use when two parents share the same method name. Python resolves this using the **MRO** (Method Resolution Order).

---

### MRO — Method Resolution Order

**What it is:**
The order in which Python searches through a class's inheritance chain to find a method. Python uses the C3 linearisation algorithm to determine this order.

**In Python:**
```python
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Flyable'>, <class 'Swimmable'>, <class 'object'>)
```

Python starts at the leftmost class and works its way right. If a method is not found in `Duck`, it looks in `Flyable` next, then `Swimmable`, then `object`.

---

## 🔐 Access Control

---

### Public

**What it is:**
An attribute or method that can be accessed from anywhere — inside or outside the class.

**In Python:**
Everything is public by default. `self.name` is a public attribute.

---

### Protected (`_single_underscore`)

**What it is:**
An attribute or method prefixed with a single underscore. This is a *convention* signalling "this is internal — use it with care." Python does not enforce this — it is a polite signal to other developers.

**In Python:**
```python
self._internal_value = 42  # "please don't touch this from outside the class"
```

---

### Private (`__double_underscore`)

**What it is:**
An attribute or method prefixed with two underscores. Python *actively transforms* its name (name mangling) to make it harder — though not impossible — to access from outside the class.

**In Python:**
```python
class Vault:
    def __init__(self):
        self.__secret = "hidden"  # name-mangled to _Vault__secret

v = Vault()
# v.__secret        → AttributeError
# v._Vault__secret  → works, but you really shouldn't
```

---

### Property (Getter/Setter via `@property`)

**What it is:**
A way to define methods that behave like attributes. They let you add logic (validation, computation) to what looks like simple attribute access.

**The intuition:**
You want `person.age` to look like reading a variable, but you also want to prevent someone setting `person.age = -5`. A property lets you have clean syntax on the outside and control logic on the inside.

**In Python:**
```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):             # getter — accessed like an attribute
        return self._age

    @age.setter
    def age(self, value):      # setter — runs when you assign
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value
```

---

## ✨ Special Methods (Dunder Methods)

---

### Dunder Methods

**What it is:**
Methods with double underscores on both sides (`__like_this__`). Python calls them automatically in response to built-in operations. "Dunder" = "Double UNDERscore."

**The intuition:**
When you do `len(my_object)`, Python does not look for a `len` attribute on the object — it calls `my_object.__len__()` behind the scenes. Dunder methods let you define how your objects respond to standard Python operations.

---

### `__str__` vs `__repr__`

| Method | Purpose | Called by |
|---|---|---|
| `__str__` | Human-readable string (for users) | `print()`, `str()` |
| `__repr__` | Unambiguous string (for developers) | `repr()`, interactive shell |

**In Python:**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"        # clean, readable

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"  # precise, reconstructable
```

---

### `__len__`

**What it is:**
Defines what happens when `len()` is called on your object.

**In Python:**
```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

p = Playlist(["Song A", "Song B", "Song C"])
print(len(p))  # 3
```

---

### `__eq__`

**What it is:**
Defines what "equal to" (`==`) means for your objects. Without this, Python compares object identity (memory address), not content.

**In Python:**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True (without __eq__, this would be False)
```

---

### `__iter__` and `__next__`

**What it is:**
`__iter__` makes an object iterable (usable in a `for` loop). `__next__` defines what "the next item" means.

**In Python:**
```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for number in Countdown(3):
    print(number)  # 3, 2, 1
```

---

## 🧩 Other Important Terms

---

### Abstract Class

**What it is:**
A class that cannot be instantiated directly. It exists purely to be inherited from. It defines a *contract* — a set of methods that all subclasses must implement.

**In Python:**
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):  # every subclass MUST implement this
        pass

# Animal()  → TypeError: Can't instantiate abstract class
```

---

### Abstract Method

**What it is:**
A method declared in an abstract class with no implementation. Subclasses are required to provide their own implementation. If they do not, Python raises a `TypeError`.

---

### Interface (Python's version)

**What it is:**
Python does not have a formal `interface` keyword like Java or C#. Instead, abstract classes with only abstract methods serve the same purpose — defining a contract without any implementation.

---

### Composition

**What it is:**
Building complex objects by combining simpler ones, rather than inheriting from them. "Has-a" relationship rather than "is-a".

**The intuition:**
A `Car` *has an* `Engine`. It does not *inherit from* `Engine`. Composition models ownership and collaboration; inheritance models identity.

**In Python:**
```python
class Engine:
    def start(self):
        return "Engine running"

class Car:
    def __init__(self):
        self.engine = Engine()  # composition — Car HAS AN Engine

    def start(self):
        return self.engine.start()
```

**When to use which:**
Use **inheritance** when the child class genuinely *is a* type of the parent.
Use **composition** when the class *has* or *uses* something.
If in doubt, prefer composition — it tends to produce more flexible code.

---

### Duck Typing

**What it is:**
Python's approach to polymorphism. If an object has the method you are calling, Python does not care what class it belongs to. "If it walks like a duck and quacks like a duck, it's a duck."

**The intuition:**
You do not need an object to officially declare it can `fly()`. If it has a `fly()` method, Python will call it. This is fundamentally different from languages like Java, which require formal type declarations.

**In Python:**
```python
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm quacking like a duck!"

def make_it_quack(thing):
    print(thing.quack())  # doesn't care what 'thing' is — just needs quack()

make_it_quack(Duck())    # Quack!
make_it_quack(Person())  # I'm quacking like a duck!
```

---

### Operator Overloading

**What it is:**
Defining how standard Python operators (`+`, `-`, `*`, `==`, `<`, etc.) behave when applied to your custom objects.

**In Python:**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):          # defines what + means for Vectors
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
```

---

### Mixin

**What it is:**
A small class designed to add a specific, reusable behaviour to other classes through inheritance — without being a standalone class in its own right.

**The intuition:**
Mixins are like optional add-ons. A `LoggingMixin` adds logging behaviour. A `SerializableMixin` adds the ability to convert to JSON. You mix them into whatever classes need them.

**In Python:**
```python
class LoggingMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class UserService(LoggingMixin):
    def create_user(self, name):
        self.log(f"Creating user: {name}")
```

---

### Class Method (`@classmethod`)

**What it is:**
A method that belongs to the class rather than to any specific instance. It receives the class itself (`cls`) as its first argument instead of `self`.

**Common use:** Alternative constructors.

**In Python:**
```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):   # alternative constructor
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)

d = Date.from_string("2024-05-27")
```

---

### Static Method (`@staticmethod`)

**What it is:**
A method that belongs to the class namespace but has no access to the class or instance. It receives neither `self` nor `cls`. It is essentially a regular function that lives inside a class for organisational reasons.

**In Python:**
```python
class MathUtils:
    @staticmethod
    def is_even(number):    # no self, no cls — pure function
        return number % 2 == 0

print(MathUtils.is_even(4))  # True
```

---

## 🧠 Quick Reference Cheat Sheet

```
CLASS          → The blueprint
OBJECT         → A thing built from the blueprint
INSTANCE       → Same as object — a specific realisation of a class
ATTRIBUTE      → Data stored on an object (what it knows)
METHOD         → A function on an object (what it can do)
self           → "This specific object, right here"
__init__       → Runs at creation — sets up the object

ENCAPSULATION  → Bundle + protect data
INHERITANCE    → Child class gets parent's features ("is-a")
POLYMORPHISM   → Same call, different behaviour per object
ABSTRACTION    → Hide complexity, expose simplicity

PUBLIC         → accessible everywhere (default)
_PROTECTED     → convention: internal use only
__PRIVATE      → name-mangled: harder to access externally

@property      → method that behaves like an attribute
@classmethod   → method that operates on the class itself
@staticmethod  → utility function that lives in the class

super()        → access the parent class
ABC            → abstract base class (cannot be instantiated)
@abstractmethod → forces subclasses to implement this method

Composition    → "has-a" — build with parts
Inheritance    → "is-a" — extend a type
Duck Typing    → "behaves like" — Python's flexible polymorphism
Mixin          → add-on behaviour via inheritance
```

---

## 📎 A Note on Naming

Python's OOP community uses several terms interchangeably. Here is a quick translation guide:

| Term A | Same as |
|---|---|
| Parent class | Base class, Superclass |
| Child class | Derived class, Subclass |
| Constructor | `__init__`, Initialiser |
| Dunder method | Magic method, Special method |
| Instance | Object |

They all mean the same things. Different books, tutorials, and developers prefer different vocabulary — but the concepts are identical.

---

<div align="center">

*This glossary lives in the `notes/` folder of the project.*
*When a term does not click, come back here before looking it up elsewhere.*
*Plain language first. Official documentation second.*

</div>
