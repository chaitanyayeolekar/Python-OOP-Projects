class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(Self, new_salary):

        if new_salary > 0:
            Self.__salary = new_salary
            print("Salary Updated Successfully")
        else:
            print("Invalid salary")

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount
            print("Salary Increase by Rs ",amount)
        else:
            print("Invalid Amount")


    def display(self):
        print("\n-----Employee Details------")
        print("Name :",self.name)
        print("Salary :",self.__salary)

e1 = Employee("Chaitanya",50000)

e1.display()

e1.increase_salary(10000)

e1.display()

e1.set_salary(70000)

e1.display()

print("\n Salary using Getter:", e1.get_salary())