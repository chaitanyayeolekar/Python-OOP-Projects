class Car:
    def __init__(self, brand, model, price, color):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color

    def start_car(self):
        print("car Started")

    def Stop_car(self):
        print("car stopped")

    def display(self):
        print("brand :",self.brand)
        print("model :",self.model)
        print("price :",self.price)
        print("color :",self.color)
                                



c1 = Car("bmw", "m4 compitition",15000000, "pearl white")
c1.start_car()
c1.Stop_car()
c1.display()


#Without OOP Concept 



brand = "bmw"
model = "m4 compitition "
price = 1500000
color = "pearl white"


def Start_Car():
    print("car started")

def Stop_Car():
    print("Car Stopped")

def Display():
    print("Brand :",brand)
    print("Model :",model)
    print("Price :",price)
    print("Color :",color)


Start_Car()
Stop_Car()
Display()


# *****************programm with parameterized function*********************

def start_car():
    print("Car started")

def stop_car():
    print("Car Stopped")

def Display(brand , model , price , color):
    print("brand :",brand)
    print("brand :",model)
    print("brand :",price)
    print("brand :",color)

start_car()
stop_car()
Display("bmw","m4",15000000, "black")
Display("bmw","rs 5",15000000, "pearl white")
Display("bmw","m2 compitition",20000000, "sofasticate blue")

