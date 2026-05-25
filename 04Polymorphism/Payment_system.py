class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        pass


class CreditCard(Payment):
    def pay(self):
        print(f"💳 Paid ${self.amount} using Credit Card.")


class PayPal(Payment):
    def pay(self):
        print(f"🅿 Paid ${self.amount} using PayPal.")


class Crypto(Payment):
    def pay(self):
        print(f"💲 Paid ${self.amount} using Crypto.")


def checkout(payment_method):
    print(f"Processing payment ...")
    payment_method.pay()
    print("Done!")


checkout(CreditCard(200))
checkout(Crypto(30))
checkout(PayPal(260))


# Notice: Polymorphism builds on inheritance
