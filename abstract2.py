from abc import *
class Car(ABC):
    def __init__(self,regno):
        self.regno=regno
    def openTank(self):
        print('fill the fuel into the tank')
        print(' for the car with regno',self.regno)
    @abstractmethod
    def steering(self):
        pass
    @abstractmethod
    def baanking(self):
        pass
    
