# Interface

from abc import ABC, abstractmethod

# Interface
class Flyable(ABC):
    @abstractmethod
    def take_off(self):
        pass

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        pass

# Concrete class implementing the interface
class PassengerPlane(Flyable):
    def take_off(self):
        print("Passenger Plane taking off")

    def fly(self):
        print("Passenger Plane flying")

    def land(self):
        print("Passenger Plane landing")

# Usage
def demo():
    passenger_plane = PassengerPlane()
    passenger_plane.take_off()
    passenger_plane.fly()
    passenger_plane.land()
