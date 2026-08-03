from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod

    def calculateDelieveryCharge(self):
        pass

class Zomato(Delivery):
    def __init__(self,amount):
        self.amount = amount

    def calculateDelieveryCharge(self,km):
        charge = self.amount * km
        print("your delivery charges are:",charge)


        
class Swiggy(Delivery):
    def __init__(self,amount):
        self.amount = amount

    def calculateDelieveryCharge(self,km):
        charge = self.amount * km
        print("your delivery charges are:",charge)

c1 = Zomato(20)
c1.calculateDelieveryCharge(5)
c1.calculateDelieveryCharge(2)

s1 = Swiggy(50)
s1.calculateDelieveryCharge(10)


#**************************Advance Polymorphism program*************************


from abc import ABC, abstractmethod

class Delivery(ABC):

    def __init__(self,distance):
        self.distance = distance

    @abstractmethod
    def calculateDeliveryCharge(self):
        pass

class Zomato(Delivery):
    def calculateDeliveryCharge(self):
        charge = 30 + (self.distance * 8)
        return charge

class Swiggy(Delivery):

    def calculateDeliveryCharge(self):
        charge = 20 + (self.distance * 10)
        return charge

z1 = Zomato(5)
s1 = Swiggy(5)

print("Zomato Charge :",z1.calculateDeliveryCharge)
print("Swiggy Charge :",s1.calculateDeliveryCharge)