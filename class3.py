class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def getMarks(self):
        return self.marks
n=int(input('how many students? '))
i=0
while(i<n):
    s=Student()
    name=input('enter name:')
    s.setName(name)
    marks=int(input('enter marks:'))
    s.getMarks(marks)
    print('hi',s.getName())
    print('your marks',s.getMarks())
    i+=1
    print('-------------------------')
