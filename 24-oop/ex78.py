class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, quantity):
        self.balance += quantity
        return self.balance

    def withdraw(self, quantity):
        self.balance -= quantity
        return self.balance

    def get_balance(self):
        return self.balance
