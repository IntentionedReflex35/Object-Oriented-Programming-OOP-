class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner.capitalize()
        self.__balance = balance

    def get_balance(self):
        print(f"{self.owner}'s balance: ${self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}✅")
        else:
            print(f"Invalid amount❌")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Insufficient funds❌")
        elif amount <= 0:
            print(f"Invalid amount❌")
        else:
            self.__balance -= amount
            print(f"Withdrawn ${amount}")


account = BankAccount("ike", 5000)

account.get_balance()

account.deposit(2500)
account.get_balance()

account.withdraw(3698)
account.get_balance()

account.withdraw(999999)

# Try to break in
account.__balance = -9999999
print(account.__balance)  # this successfully gets printed but ...
account.get_balance()  # the original balance or balance after any withdrawal or deposit is however, still kept intact
