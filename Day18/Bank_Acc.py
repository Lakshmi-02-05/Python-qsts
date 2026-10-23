
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount must be positive")

    def get_balance(self):
        return self.__balance

account = BankAccount("Lakshmi")

account.deposit(1000)
account.deposit(500)

print("Account Holder:", account.name)
print("Final Balance:", account.get_balance())
