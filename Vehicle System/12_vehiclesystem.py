class Vehicle:

    def start(self):
        print("vehicle start")

    def stop(self):
        print("Vehicle Stop")

    def calculateMileage(self):
        print("Vehicle mileage")

class Bike(Vehicle):
    def calculateMileage(self):
        print("Bike Mileage :45km/l")


class Car(Vehicle):
    def calculateMileage(self):
        print("Car Mileage: 18 km/l")

class Truck(Vehicle):
    def calculateMileage(self):
        print("Truck Mileage : 8 km/l")

b1 = Bike()
c1 = Car()
T1 = Truck()

b1.calculateMileage()
c1.calculateMileage()
T1.calculateMileage()