# Abstract Class
# Shares state and behaviour with its subclasses ("is a" relationship).

from abc import ABC, abstractmethod


class Plane(ABC):
    def __init__(self, name: str):
        self.name = name  # shared state

    # shared, concrete behaviour (a template method)
    def flight(self):
        self.take_off()
        print(f"{self.name} flying")
        self.land()

    # steps that every subclass must implement
    @abstractmethod
    def take_off(self): ...

    @abstractmethod
    def land(self): ...


class PassengerPlane(Plane):
    def take_off(self):
        print(f"{self.name} taking off from the runway")

    def land(self):
        print(f"{self.name} landing on the runway")


class Seaplane(Plane):
    def take_off(self):
        print(f"{self.name} taking off from the water")

    def land(self):
        print(f"{self.name} landing on the water")


# Usage
def demo():
    # Plane("x")  # TypeError: can't instantiate an abstract class
    for plane in (PassengerPlane("Passenger Plane"), Seaplane("Seaplane")):
        plane.flight()
