class father:
    def height(self):
        print('height is 6.0 foot')
class mother:
    def color(self):
        print('color is brown')
class child(father,mother):
    pass

c=child()
print('child \'s inherited qualities:')
c.height()
c.color()
