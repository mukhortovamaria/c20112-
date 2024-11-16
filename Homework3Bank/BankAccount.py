class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} грн внесено на рахунок {self.account_number}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = amount
            print(f"{amount} грн знято з рахунку {self.account_number}.")
        else:
            print("Недостатньо коштів.")

    def __str__(self):
        return f"{self.owner} | N{self.account_number} | Баланс: {self.balance} грн"