class Student:

    def __init__(self):
        self.filename = "student.txt"

    def add_student(self, roll, name , marks):

        file =  open(self.filename,"r")

        for line in file:
            data = line.strip().split(",")

            if data[0] == str(id):
                print("Student already exist")
                file.close()
                return
        file.close()
                
        file = open(self.filename,"a")
        file.write(f"{roll},{name},{marks}\n")
        file.close()

        print("Student Added Successfully")


    def search_student(self, roll):

        file = open(self.filename,"r")

        found = False

        for line in file:
            data = line.strip().split(",")

            if data[0] == str(roll):

                print("\nStudent Found")
                print("Roll :", data[0])
                print("Name :", data[1])
                print("Makrs :",data[2])

                found = True
                break

        if found == False:
            print("Student Not found")
        file.close()

s1 = Student()

while True:

    print("\n------Student Record System--------")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Exit")

    choice = int(input("Enter Choice"))

    if choice == 1:

        roll = int(input("Enter Roll : "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks : "))

        s1.add_student(roll, name, marks)

    elif choice == 2:
        roll = int(input("Enter Roll Number : "))    
        s1.search_student(roll)

    elif choice == 3:
        print("thank you")
        break

    else:
        print("Invalid choice")                    