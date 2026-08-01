class Mobile:
    def __init__(self, brand, ram , storage, battery):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.battery = battery

    def Call(self):
        print("incoming Call")

    def Charge(self, charging):
        if charging >= 20:
            print("sufficient")
        else:
            print("battery low please charge the phone")

    def Display_spec(self):
        print("brand :", self.brand)
        print("ram :", self.ram)
        print("storage :", self.storage)
        print("battery :", self.battery)

m1 = Mobile("Apple","8 gb","128gb","4800MAH")
m1.Call()
m1.Charge(50)
m1.Display_spec()

        

#**************************Without OOp Concept***************************



def call():
    print("incoming Call")
def Charge(batteryhealth):
    if batteryhealth >= 20:
        print("enough battery")
    else:
        print("battery low")
    

def mobile(brand, ram, storage, battery):
    print("brand :",brand)
    print("ram :", ram)
    print("Storage :",storage)
    print("battery :",battery)


call()
Charge(50)
mobile("apple",8,128,"4800mah")