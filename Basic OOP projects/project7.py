class Atm:

    def __init__(self,acc_no, name, pin,balance):
        self.acc_no = acc_no
        self.name = name
        self.pin = pin
        self.balance = balance

    def login(self, pin):
        if pin == self.pin:
            print("login successfully")
        else:
            print("incorrect Password")
        
       
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Amount Deposited :", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Available balances is :", self.balance)

    def balance_inquiry(self):
        print("Current Balance: ", self.balance)

    def MiniStatement(self):
        print("the acc no      :",self.acc_no)
        print("the person is   :",self.name)
        print("Current Balance :", self.balance)
        print("total balance   :",self.balance)

A1 = Atm(101, "Chaitanya", 2004, 50000)
A1.login(2004)
A1.deposit(10000)
A1.withdraw(20000)
A1.MiniStatement()




#***************************spphisticated way**********************************#
#brute force


class ATM:

    def __init__(self, acc_no, name, pin, balance):
        self.acc_no = acc_no
        self.name = name
        self.pin = pin
        self.balance = balance
        self.logged_in= False

    def login(self, entered_pin):

        if entered_pin == self.pin:
            self.logged_in = True
            print("login Successfully")
        else:
            print("incorrect Password")


    def deposit(self, amount):

        if self.logged_in:

            self.balance += amount
            print(amount, "Deposited Successfully")

        else:
            print("Please Login First")

    def withdraw(self, amount):

        if self.logged_in:

            if amount <= self.balance:
                self.balance -= amount
                print(amount, "Withdrawn Successfully")

            else:
                print("please Login first")

    def balance_inquiry(self):

        if self.logged_in:
            print("Current balance :",self.balance)

        else:
            print("please Login First")

    def mini_statement(self):

        if self.logged_in:

            print("\n------MINI STATEMENT--------")
            print("Account Number :",self.acc_no)
            print("Name:",self.name)
            print("Current Balance",self.balance)
        else:
            print("please Login first")

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            print("logout Successfully")
        else:
            print("you are not logged in")


A1 = ATM(101, "Chaitanya",2004,5000)

A1.login(2004)
A1.deposit(10000)
A1.withdraw(15000)
A1.balance_inquiry()
A1.mini_statement()
A1.logout






#optimal solution 