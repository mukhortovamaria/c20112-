from Bank import Bank
from BankAccount import BankAccount
bank = Bank()
acc1 = BankAccount(owner="Маша", account_number="001", balance=10000)
acc2 = BankAccount(owner="Настя", account_number="002", balance=5000)
bank.add_account(acc1)
bank.add_account(acc2)
acc1.deposit(2000)
acc2.withdraw(1500)
bank.transfer("001", "002", 3000)
bank.show_accounts()