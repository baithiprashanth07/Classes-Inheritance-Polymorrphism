class Student:
    def __init__(self,n='',m=0):
        self.name=n
        self.marks=m
    def display(self):
        print('hi',self.name)
        print('your marks', self.marks)
    def calculate(self):
        if(self.marks >=600):
            print('you got first grade')
        elif(self.marks >=500):
                print(' you got second grade')
        elif(self.marks >=350):
                print('you got third grade')
        else:
                print('you failed')
n= int(input('how many students? '))
i=0
while(i<n):
    name=input('enter name:')
    marks=int(input('enter marks:'))
    s=Student(name,marks)
    s.display()
    s.calculate()
    i+=1
    print('----------------')
            
