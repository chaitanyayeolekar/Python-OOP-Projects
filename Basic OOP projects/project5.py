class Employee:
    def __init__(self, name , id , basic_salary):
        self.name = name
        self.id = id
        self.basic_salary = basic_salary

    def Calculate_bonus(self):
        bonus = self.basic_salary/5
        self.basic_salary = bonus + self.basic_salary
        print(bonus)

    def Display_salary(self):
        print("name of the employee is :", self.name)
        print("id of the employee is :", self.id)
        print("the total salary with bonus is ",self.basic_salary)

s1 = Employee("chaitanya", 120,50000)
s1.Calculate_bonus()
s1.Display_salary()

        
