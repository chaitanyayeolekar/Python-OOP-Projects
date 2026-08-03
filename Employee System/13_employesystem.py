class Employee:

    def __init__(self,basic_salary):
        self.basic_salary = basic_salary

    def calculatesalary(self):
        print("Employee salary")

class Manager(Employee):

    def calculatesalary(self,bonus):
        total_salary = self.basic_salary + bonus
        print("Manager salary :",total_salary)

class Developer(Employee):

    def calculatesalary(self,bonus):
        total_salary = self.basic_salary + bonus
        print("Developer Salary:", total_salary)

class Intern(Employee):

    def calculatesalary(self):
        total_salary = self.basic_salary
        print("Intern Salary:", total_salary)


e1 = Employee(50000)

M1 = Manager(50000)
M1.calculatesalary(10000)

d1 = Developer(40000)
d1.calculatesalary(5000)

i1 = Intern(30000)
i1.calculatesalary()