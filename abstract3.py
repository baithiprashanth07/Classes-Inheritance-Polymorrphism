from abc import Car
class Maruti(car):
    def steering(self):
        print('Maruti uses manual steering')
        print('Drive the car')
    def banking(self):
        print('Maruti uses hydraulic brakes')
        print('Apply brakes and stop it')
m=Maruti(1001)
m.openTank()
m.steering()
m.breaking()
