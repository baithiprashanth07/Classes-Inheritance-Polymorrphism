class bank:
    def __init__(self):
        self.accno=10
        self.name='srinu'
        self.balance=5000.00
        self.__loan=1500000.00
    def display_to_clerk(self):
        print(self.accno)
        print(self.name)
        print(self.balance)
        
