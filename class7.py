class emp:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        print('id=',self.id)
        print('name=',self.name)
        print('salary=',self.salary)

class Myclass:
    @staticmethod
    def mymethod(e):
        e.salary+=1000;
        e.display()
e=emp(10,'prashanth',15000.75)
Myclass.mymethod(e)
