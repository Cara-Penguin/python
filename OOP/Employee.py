# Name : 柯玲萱 Cara
# ID : 10890021

class Employee:
    count = 0

    def __init__(self,name, salary) -> None:
        self.name = name
        self.salary = salary
        Employee.count = Employee.count +1

    def displayCount(self):
        print("Total Employee: {}".format(self.count))


    def displayEmployee(self):
        print("Name : {}  , Salary: {}".format(self.name,self.salary))

first = Employee("Zara", 2000) 
second = Employee("Manni", 5000) 

first.displayEmployee()
second.displayEmployee()
second.displayCount()

