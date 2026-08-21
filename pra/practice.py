# class Vehicle:
#     def start(self):
#         print("Vehicle Start")


# class Car(Vehicle):
#     pass

# class Bike(Vehicle):
#     pass

# c1 = Car()
# b1 = Bike()

# c1.start()
# b1.start()



#****************************Another Example*******************************

# class Employee:

#     def work(self):
#         print("Working")

# class Developer(Employee):
#     pass

# c1 = Employee()
# c1.work()

# c1 = Developer()


# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass

# class UPI(Payment):

#     def pay(self):
#         print("Payment Through UPI")


# class CreditCard(Payment):

#     def pay(self):
#         print("Payment through credit Card")


# u1 = UPI()
# c1 = CreditCard()

# u1.pay()
# c1.pay()



# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def pay(self):
#         pass

# class UPI(Payment):

#     def __init__(self, amount):
#         self.amount = amount

#     def pay(self):
#         print("UPI Payment :", self.amount)

# class CreditCard(Payment):

#     def __init__(self, amount):
#         self.amount = amount

#     def pay(self):
#         print("credit Card Payment :",self.amount)

# u1 = UPI(500)
# c1 = CreditCard(1000)

# u1.pay()
# c1.pay()

# #***************************Real Polymorphism******************************

# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def pay(self):
#         pass

# class UPI(Payment):
#     def pay(self):
#         print("UPI Payment")

# class CreditCard(Payment):
#     def pay(self):
#         print("Credit Card Payment")

# class DebitCard(Payment):
#     def pay(self):
#         print("Debit Card Payment")

# payments = [
#     UPI(),
#     CreditCard(),
#     DebitCard()
# ]

# for payment in payments:
#     payment.pay()


#**************************Advance level***************************


# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# shapes = [
#     Circle(5),
#     Square(6)
# ]

# for shape in shapes:
#     print(shape.area())


#====================Dictionary===================


# students = {
#     "Chaitanya":85,
#     "Rahul": 70,
#     "Amit": 89,
#     "dnyanesh":90
# }

# name = input("Enter Student name :")
# marks = int(input("Enter your marks"))

# if name in students:
#     students[name] = marks

#     print("Makrs not found")

# else:

#     print("Student Not Found")

# for student in students:

#     print(student, students[student])


# products = {
#     "Laptop": 50000,
#     "Mobile": 20000,
#     "Headphones": 2000,
#     "Keyboard": 1500
# }
# print("=========Product List===========")

# #Search Product
# print("==========SEARCH PRODUCT=========")

# for product in products:
#     print(product, products[product])

# found = False
# prod = input("Enter You Product : ")

# if prod in products:
#     found = True
#     print(prod, "price :",products[prod])
# else:
#     found = False
#     print("Rproduct Not Found")

# #Add Product
# print("===========ADD PRODUCT IN LIST==============")

# name = input("Enter Product Name : ")
# price = int(input("Enter product prices : "))

# products[name] = price
# print("Product Added Successfully")

# print("Generate New List")

# for product in products:
#     print(product, products[product])


# #Update Product
# print("=============UPDATEproduct============")

# name = input("Enter Product Name : ")
# price = int(input("Enter product prices : "))

# if name in products:
#     found = True
#     products[name]=price
#     print(products[name],"price Updated Successfuly")
# else:
#     print("Product Not Found")

# for product in products:
#     print(product,products[product])

# #delete Product
# print("=======DELETE PRODUCT=============")

# name = input("Enter Product Name : ")

# if name in products:
#     del products[name]
#     print("product deleted successfully")
# else:
#     print("Product Not Found")

# for product in products:
#     print(product, products[product])


# questions = {
#     1:{
#         "question":"what is 5 + 5",
#         "options":["5","10","15","20"],
#         "answer":"b"
#     }
# }

# letters = ["a","b","c","d"]

# print(questions[1]["question"])

# for i in range(4): 
#     print(letters[i],".",questions[1]["options"][i])

# answer = input("Enter your Answer : ")

# if answer.upper() == questions[1]["answer"].upper():
#     print("Correct Answer!")

# else:
#     print("Wrong Answer!")                     


# class Practice:

#     def information(self):
#         name = "chaitanya"
#         age = 15
#         brand = "addidas"
#         function = "hacker ofcourse"

        

#     def call(self,name , age , brand , function):
#         print(name)
#         print(age)
#         print(brand)
#         print(function)

# c1 = Practice()
# c1.information()
# c1.call()


# class Student:

#     def save_marks(self, name, marks):
#         print("Student",name)
#         print("Makrs",marks)

#     def result(self):

#         student_name = "Chaitanya"
#         student_marks = "85"

#         self.save_marks(student_name,student_marks)
# s1 = Student()
# s1.result()


print("-" * 65)

print(
    f"{'Room':<8}"
    f"{'type':<15}"
)