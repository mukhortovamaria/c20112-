class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print(f" {account.account_number} додано до банку.")

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].balance -= amount
                self.accounts[to_acc].balance += amount
                print(f"{amount} грн переказано з {from_acc} на {to_acc}.")

    def show_accounts(self):
        for account in self.accounts.values():
            print(account)