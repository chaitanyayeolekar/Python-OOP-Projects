class BankAccount:
    def __init__(self, acc_no, name , balance):
        self.acc_no=acc_no
        self.name = name
        self.balance=balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("amount Deposited:", amount)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Amount Withdrawan: ", amount)

    def checkbal(self):
        print("Current Balance",self.balance)

a1 = BankAccount(101, "Chaitanya", 50000)
a1.deposit(20000)
a1.withdraw(60000)
a1.checkbal()

#without OOP concept 

acc_no = 101
name = "Chaitanya"
balance = 5000

def deposit(amount):
    balance = balance + amount
    print(amount)


def withdraw(amount):
    global balance
    if amount <=balance:
        balance = balance - amount
        print(amount)
    else:
        print("no balance")

def check_balance():
    print("balance")

deposit(2000)
withdraw(5000)
check_balance()

