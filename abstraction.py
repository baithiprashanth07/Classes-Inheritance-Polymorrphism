class Myclass():
    def __init__(self):
        self.x=1
        self.__y=2
    def display(self):
        print(self.x)
        print(self._Myclass__y)
    print('accessing variables through method:')
    m=Myclass()
    m.display()
    print('accessing variables throught method:')
    print(m.x)
    print(m._Myclass__)
