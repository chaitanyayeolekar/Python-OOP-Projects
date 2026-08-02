#grocery management

class Product:

    def __init__(self,product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class Cart:

    def __init__(self):
        self.total = 0

    def add_product(self,product):
        self.total +=product.price
        print(product.name,"Added to Cart")

    def remove_product(self, product):
        self.total -= product.price
        print(product.name,"Removed from cart")

    def total_bill(self):
        print("Total Bill : RS",self.total)

p1 = Product(101,"Mouse",500)
p2 = Product(102,"Keyboard",1500)
p3 = Product(103,"wire",2000)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

cart.total_bill()

cart.remove_product(p2)

cart.total_bill()



#***********************recreate the program**************************


class Product: 


    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class Cart:


    def __init__(self):
        self.total = 0

    def Add_product(self,product):
        self.total = self.total + product.price
        print(product.name, "Added to cart ")

    def remove_product(self,product):
        self.total = self.total - product.price
        print(product.name,"remove from the cart")

    def total_bill(self):

        print("total bill is rs :",self.total)


p1 = Product(1,"Mouse",500)
p2 = Product(2,"keyboard",1500)
p3 = Product(3,"wire",2000)


c1 = Cart()
c1.Add_product(p1)
c1.Add_product(p2)
c1.Add_product(p3)

c1.total_bill()

c1.remove_product(p2)

c1.total_bill()
