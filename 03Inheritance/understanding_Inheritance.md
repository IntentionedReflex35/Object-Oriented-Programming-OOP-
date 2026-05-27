# Pillar 2 — Inheritance
Think about animals.

A dog can bark, eat and sleep.

A cat can meow, eat and sleep.

A bird can chirp, eat and sleep.

Notice something? Eating and sleeping is common to all of them.

Now imagine you are coding this without inheritance:
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says: Woof!")

    def eat(self):
        print(f"{self.name} is eating ...")

    def sleep(self):
        print(f"{self.name} is sleeping ...")


class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} says: Woof!")

    def eat(self):
        print(f"{self.name} is eating ...")

    def sleep(self):
        print(f"{self.name} is sleeping ...")


class Bird:
    def __init__(self, name):
        self.name = name

    def chirp(self):
        print(f"{self.name} says: Woof!")

    def eat(self):
        print(f"{self.name} is eating ...")

    def sleep(self):
        print(f"{self.name} is sleeping ...")
```

---

**You see the problem:**

`eat()` and `sleep()` are repeated in every single class. Imagine you have 50 animal types. That's eat() and sleep() written
50 times.
You would even find it difficult when it comes to editing the messages.

**ROOT CAUSE:**

We are repeating common behaviour across multiple classes instead of writing it once and sharing it.

See `Animal_practice.py` for solution to this problem.
