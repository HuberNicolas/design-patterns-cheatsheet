# Interface
# Python has no interface keyword. Two common ways to define a contract
# that unrelated classes can fulfil ("can do" relationship):

from abc import ABC, abstractmethod
from typing import Protocol


# 1. Abstract base class without state or implementation (explicit: classes inherit it)
class Flyable(ABC):
    @abstractmethod
    def take_off(self): ...

    @abstractmethod
    def fly(self): ...

    @abstractmethod
    def land(self): ...


class PassengerPlane(Flyable):
    def take_off(self):
        print("Passenger Plane taking off")

    def fly(self):
        print("Passenger Plane flying")

    def land(self):
        print("Passenger Plane landing")


class Bird(Flyable):
    def take_off(self):
        print("Bird taking off")

    def fly(self):
        print("Bird flapping its wings")

    def land(self):
        print("Bird landing on a branch")


# 2. Protocol (structural: any class with matching methods fits, no inheritance needed)
class Swimmer(Protocol):
    def swim(self) -> str: ...


class Duck:
    def swim(self) -> str:
        return "Duck paddling"


def go_swimming(swimmer: Swimmer):
    print(swimmer.swim())


# Usage
def demo():
    flyers: list[Flyable] = [PassengerPlane(), Bird()]
    for flyer in flyers:
        flyer.take_off()
        flyer.fly()
        flyer.land()

    go_swimming(Duck())  # Duck never mentions Swimmer, a type checker still accepts it
