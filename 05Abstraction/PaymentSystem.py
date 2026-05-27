from abc import ABC, abstractmethod

# =============================================
#   ABSTRACT CLASS — the enforced contract
# =============================================


class Payment(ABC):             # 👈 inherits from ABC

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod             # 👈 this MUST be implemented by children
    def pay(self):
        pass

    @abstractmethod             # 👈 this MUST be implemented too
    def get_receipt(self):
        pass


# =============================================
#   CHILD CLASSES — must follow the contract
# =============================================

class CreditCard(Payment):
    def pay(self):
        print(f"💳 Paid ${self.amount} via Credit Card")

    def get_receipt(self):
        print(f"📧 Credit Card receipt sent to your email")


class PayPal(Payment):
    def pay(self):
        print(f"🅿️  Paid ${self.amount} via PayPal")

    def get_receipt(self):
        print(f"📧 PayPal receipt sent to your PayPal email")


# =============================================
#   WHAT HAPPENS IF SOMEONE FORGETS? 👀
# =============================================

"""
class Crypto(Payment):
    def pay(self):
        print(f"₿  Paid ${self.amount} via Crypto")

    # 😬 forgot to implement get_receipt()!


crypto = Crypto(300)
# 💥 TypeError: Can't instantiate abstract class Crypto
#    because it doesn't implement 'get_receipt'

# Python immediately throws an error the moment someone tries to use an incomplete class.
# No surprises later. No silent bugs. Caught right away. ✅
"""


# And the full thing working correctly:
class Crypto(Payment):
    def pay(self):
        print(f"₿  Paid ${self.amount} via Crypto")

    def get_receipt(self):              # ✅ now complete
        print(f"📧 Crypto receipt saved to blockchain")


# =============================================
#   NOW EVERYTHING WORKS BEAUTIFULLY
# =============================================

payments = [
    CreditCard(100),
    PayPal(200),
    Crypto(300)
]

for payment in payments:
    payment.pay()           # same call, each handles it their own way
    payment.get_receipt()   # guaranteed to exist on ALL of them
    print("---")
