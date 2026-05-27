# Pillar 3 — Polymorphism

Think about the word **speak**.

You ask a dog to speak, it `barks`. 

You ask a cat to speak, it `meows`. 

You ask a bird to speak, it `chirps`. 

You ask a human to speak, it `talks`.

Here, there is one instruction — **speak**, but different behaviour depending on who you're talking to.

That's **polymorphism** in real life. One action, many forms.

---

### The problem without it.

Let's say you have a bunch of animals, and you want to make them all speak. Without polymorphism, you'd probably write
something like this:
```python
def make_it_speak(animal):
    if animal == "dog":
        print("Woof")
    elif animal == 'cat':
        print('Meow')
    elif animal == 'bird':
        print("Tweet")
    elif animal == 'cow':
        print("Moo")
    # ... and so on 😩

make_it_speak("dog")
make_it_speak('cow')
make_it_speak('bird')
make_it_speak('cat')
```

### What is wrong here?

Every time you add a new animal, you have to come back and add another elif here. This function grows and becomes
messier.

**How do we fix this?**

See `Animal_example.py` for continuation.
