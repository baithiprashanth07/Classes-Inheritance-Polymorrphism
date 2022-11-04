class Father:
    def __init__(self):
        self.property=800000.00
    def display_property(self):
        print('father \'s property=',self.property)
class son(Father):
    def __init__(self):
        self.property=20000.00
    def display_property(self):
        print('child \'s property=',self.property)
        
    pass
s=son()
s.display_property()
    
