# ques - create Account class with 2 attributes - balance and account number 
# create methods for debit, credit and printing the balance

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited new balance =", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was debited new balance =", self.balance)

acc1 = Account(10000, 1)
acc1.debit(4000)
acc1.debit(2000)
acc1.credit(8000)
acc1.credit(6000)