# Pillar 4 — Abstraction

**_Let's use a phone as an analogy_**

When you want to take a photo, you open the camera app. Point. Tap. Done. But behind that one tap:

- The processor wakes up the camera sensor
- Autofocus algorithm runs
- Light levels are calculated
- Image is compressed into JPEG format
- FIle is written to storage
- Thumbnail is generated for the gallery

You realise you didn't have to think about any of these processes. You just tapped. The complexity was hidden from you. 

That's **Abstraction**.

**_Another example — your car_**

You want to go forward. You press the accelerator. but behind that pedal:

- Fuel injects fire
- Pistons compress and combust
- Crankshaft converts energy to rotation
- Transmission adjusts gear ratios
- Power is delivered to the wheels

All these, you don't need to know. You just press the pedal.

> Abstraction = hide the complex stuff. Show only what the user needs.

---

### The problem without Abstraction

Imagine you're building system where other developers on your team need to create new payment types. You create the
parent class like this:

```python
class Payment:
    def __init__(self, amount):
        self.amount = amount

    # You intend for every child to define this
    # BUt you have no way to enforce it
    def pay(self):
        pass


# Now your teammate creates a new payment type:
class CreditCard(Payment):
    def process(self):
        print(f"Paid ${self.amount} via Credit Card.")


class PayPal(Payment):
    def make_payment(self):
        print(f"Paid ${self.amount} via PayPal.")


class Crypto(Payment):
    pass


# Now when you try to use polymorphism:
payments = [CreditCard(200), PayPal(700), Crypto(300)]

for payment in payments:
    payment.pay()        # BREAKS but not entirely. No output is produced. Nobody consistently implemented pay().
```

> There's no way to enforce that child classes must implement certain methods. The parent just has `pass` and hopes
everyone follows the rules.

---

### The FIX

Python gives us a tool called ABC (Abstract Base Class)

See `PaymentSystem.py` for proper code.

---

### So how is Abstraction different from Encapsulation?

|               |          🔒Encapsulation           |                        Abstraction🫙                         |
|---------------|:----------------------------------:|:------------------------------------------------------------:|
| What it hides |  Internal data (like `__balance`)  | Internal complexity (like how pay() works behind the scenes) |
| Why it hides  | To protect data from being misused |   To simplify what the outside world needs to think about    |
| Analogy       |   Bank vault — hide the money 💰   |          ATM interface — hide the banking system 🏧          |


> Encapsulation: "You can't touch this data directly."

> Abstraction: "You don't need to know how this works internally. Just call the method."
