class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("name:",self.name)
        print("name:",self.roll)
        print("name:",self.marks)

    def grade(self):

        if self.marks >= 90:
            print("grade : A")

        elif self.marks >= 75:
            print("grade : B")

        elif self.marks >=60:
            print("Grade : c")

        elif self.marks >=40:
            print("grade : d")

        else:
            print("FAil")

s1 = Student("Chaitanya",21,40)

s1.display()
s1.grade()



class Student:
    def __init__(abc, name , roll, marks):
        abc.name = name
        abc.roll = roll
        abc.marks = marks

    def display(abc):
        print("name is: ",abc.name)
        print("name is: ",abc.roll)
        print("name is: ",abc.marks)

    def grade(abc):
        if abc.marks >= 90:
            print("grade A")

        elif abc.marks >= 70:
            print("grade B")

        elif abc.marks >= 60:
            print("grade C")

        elif abc.marks >= 40:
            print("grade D")

        else:
            print("Fail")


s1 = Student("Chaitanya",21,98)

s1.display()
s1.grade()


                    
