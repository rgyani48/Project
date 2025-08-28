#Banking System
class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no
       
    def check_balance(self):
        print(f"Total balance : {self.balance}")   

    def debit(self, amount):
        self.amount = amount
        self.balance -= self.amount
        print(f"The debited amoount from account no {self.acc_no} is {self.amount} \ncurrently avilable balance is {self.balance}")
        

    def credit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f"The credited amoount in account no {self.acc_no} is {self.amount} \ncurrently avilable balance is {self.balance}")


Account1 = Account(10000, 25450110074275)
Account1.check_balance()
Account1.debit(1000)
Account1.credit(100000)