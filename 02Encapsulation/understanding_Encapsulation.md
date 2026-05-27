# Pillar 1 — Encapsulation

Imagine you're using an 🏧ATM machine. You walk up, insert your card, type your PIN and hit "Withdraw $500". 

Money comes out. Done. But here is the thing — You did not have to worry about how the ATM verified your PIN internally.

You did not have to manually check the bank's database yourself. You did not have to calculate whether your balance was
sufficient.

You just pressed a button. The ATM handled everything internally.

---

### The problem without it

Let's say you're building a BankAccount system. Without encapsulation, someone could just do this: 

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # anyone can touch this


account = BankAccount("Ali", 2000)
# anyone can just do this
account.balance = -999999
print(account.balance)
```
 
>There's nothing protecting the balance.
This is where encapsulation is needed. It hides the internal data and only allows the outside world interact through 
controlled methods like the **front desk**.

---

### THE FIX
In python, we use a double underscore `__` to make something private.

See `BankAccount_practice.py` for correct representation of encapsulation.
