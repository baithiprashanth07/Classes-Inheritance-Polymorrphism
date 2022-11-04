class Myclass:
    def sum(self,a=None, b=None,c=None):
        if a!=None and b!=None and c!=None:
            print('sum of three=',a+b+c)
        elif a!=None and b!=None:
            print('sum of two =', a+b)
        else:
            print('please enter two or three agguments')
m=Myclass()
m.sum(10,15,20)
m.sum(10.5,25.55)
m.sum(100)
