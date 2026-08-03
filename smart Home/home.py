from abc import ABC, abstractmethod

class Appliance(ABC):

    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass

class Fan(Appliance):

    def turnOn(self):
        print("Fan is ON")

    def turnOff(self):
        print("Fan is OFF")

class Tv(Appliance):

    def turnOn(self):
        print("Fan is ON")

    def turnOff(self):
        print("Fan is OFF")

class Ac(Appliance):

    def turnOn(self):
        print("Fan is ON")

    def turnOff(self):
        print("Fan is OFF")

appliances = [
    Fan(),
    Ac(),
    Tv()
]

for appliance in appliances:
    appliance.turnOn()
    appliance.turnOn()
    print("----------")