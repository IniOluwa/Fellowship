# OOP Lab
class BankAccount(object):

    def withdraw(self):
        pass

    def deposit(self):
        pass


class SavingsAccount(BankAccount):

    def __init__(self):
        balance = 500
        self.balance = balance

    def deposit(self, to_be_deposited):
        if to_be_deposited < 0:
            return "Invalid deposit amount"
        self.balance += to_be_deposited
        return self.balance

    def withdraw(self, to_be_withdrawn):
        if to_be_withdrawn < 0:
            return "Invalid withdraw amount"
        elif to_be_withdrawn > self.balance - 500:
            return "Cannot withdraw beyond the current account balance"
        elif self.balance - to_be_withdrawn < 500:
            return "Cannot withdraw beyond the minimum account balance"
        self.balance -= to_be_withdrawn
        return self.balance


class CurrentAccount(BankAccount):

    def __init__(self):
        balance = 0
        self.balance = balance

    def deposit(self, to_be_deposited):
        if to_be_deposited < 0:
            return "Invalid deposit amount"
        self.balance += to_be_deposited
        return self.balance

    def withdraw(self, to_be_withdrawn):
        if to_be_withdrawn < 0:
            return "Invalid withdraw amount"
        elif to_be_withdrawn > self.balance:
            return "Cannot withdraw beyond the current account balance"
        self.balance -= to_be_withdrawn
        return self.balance
