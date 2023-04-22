class Account:
    def __init__(self, name):
        self._account_name = name
        self._account_balance = 0

    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            self._account_balance += amount

    def get_name(self):
        return self._account_name

    def get_balance(self):
        return self._account_balance

    def withdraw(self, amount):
        if amount <= 0:
            return False
        elif amount >= self._account_balance:
            return False
        else:
            self._account_balance -= amount
