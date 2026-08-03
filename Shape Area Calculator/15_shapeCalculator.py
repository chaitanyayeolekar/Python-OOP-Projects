class Shape:
    def area(self):
        print("Calculate the Area")

class Circle(Shape):

    def area(self, radius):
        area  = 3.14*radius*radius
        print("area of circle is :",area)

class Rectangle(Shape):

    def area(self, length, width):
        area = length * width 
        print("area of rectange is :", area)

class Square(Shape):

    def area(self, length):
        area = length * length
        print("Area of square is :", area)

class Triagle(Shape):
    def area(self, base , height):
        area = 0.5 * base * height
        print("area of triabgle is ", area)

#define object
s1 = Shape()
s1.area()


c1 = Circle()
r1 = Rectangle()
s2 = Square()
t1 = Triagle()

c1.area(7)
r1.area(8,5)
s2.area(10)
t1.area(10,8)



#***********************professional program**************************

