class BankLocker:
    def __init__(self, password, balance):
        self.__balance = balance
        self.__password = password

    def check_balance(self):
        print("Balance :",self.__balance)

    def change_password(self, old_password,new_password):
        if old_password == self.__password:
            print("Password changed Successfully")

        else:
            print("Incorrect old Password")


l1 =  BankLocker(1234, 50000)
l1.check_balance()
l1.change_password()