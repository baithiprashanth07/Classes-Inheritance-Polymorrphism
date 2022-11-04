import sys
class bank(object):
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            print('balance amount is less, so no withdrawal.')
        else:
            self.balance-=amount
        return self.balance
name=input('enter name')
b=bank(True)
while(True):
    print('d -deposite,w _withdraw, e -Exit')
    choice=input('your choice:')
    if choice== 'e' or choice == 'E':
        sys.exit()
    amt=float(input('enter amount:'))
    if choice=='d' or choice =='D':
        print(' balance after deposite:',b.deposit(amt))
    elif choice=='w' or choice == 'W':
        print('balance after withdrawal:',b.withdraw(amt))
    
