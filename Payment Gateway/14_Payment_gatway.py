class Payment:

    def pay(self, amount):
        print("Payment", amount)

class UPI(Payment):

    def pay(self, amount):
        print("UPI Payment:", amount)


class CreditCard(Payment):

    def pay(self, amount):
        print("Credit card Payment:",amount)


class DebitCard(Payment):

    def pay(self, amount):
        print("Debit Card Payment :",amount)


class NetBanking(Payment):

    def pay(self, amount):
        print("Net Banking Payment :", amount)

# p1 = Payment(10000)
# p1.pay()

p1 = Payment()
p1.pay(1000000)

u1 = UPI()
c1 = CreditCard()
d1 = DebitCard()
n1 = NetBanking()

u1.pay(1000)
c1.pay(2000)
d1.pay(3000)
n1.pay(4000)