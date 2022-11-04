class person:
    def __init__(self):
        self.name='Charles'
        
    def display(self):
        print('name=',self.name)
    class Dob:
        def __init__(self):
            self.dd=10
            self.mm=5
            self.yy=1988
        def display(self):
            print('dob= {}/{}/{}'.format(self.dd,self.mm,self.yy))
p=person()
p.display()
x=person.Dob()
x.display()
print(x.yy)
