class Student:
    def __init__(self,  n= '.', m=0):
        self.name=n
        self.marks=m
    def display(self):
        print('hi',self.name)
        print('your marks',self.marks)
s=Student()
s.display()
print('--------------')
s1=Student('Lakshmi Roy',880)
s1.display()
print('----------')
