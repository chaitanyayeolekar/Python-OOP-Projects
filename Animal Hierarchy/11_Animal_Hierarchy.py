class Animal:
    def sound(self):
        print("Animal makes sound")

    def Eat(self):
        print("Animal is eating")


class Dog(Animal):

    def Sound(self):
        print("Dog says: Bow Bow")

class Cat(Animal):

    def Sound(self):
        print("cat says: meow meow")

d1 = Dog()
c1 = Cat()

d1.Sound()
d1.Eat()

c1 = Cat()
c1.sound()

