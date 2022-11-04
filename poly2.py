class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __mul__(self,other):
        return self.salary*other.days
class Attendance:
    def __init__(self,name,days):
        self.name=name
        self.days=days
x1=Employee('anil',500.00)
x2=Attendance('anil',25)
print('this month salary=',x1*x2)
