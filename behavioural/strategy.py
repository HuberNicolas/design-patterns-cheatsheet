# Strategy Pattern

from abc import ABC, abstractmethod

class FilterStrategy(ABC):

    @abstractmethod
    def removeValue(self, val):
        pass

class RemoveNegativeStrategy(FilterStrategy):

    def removeValue(self, val):
        return val < 0 

class RemoveEvenStrategy(FilterStrategy):

    def removeValue(self, val):
        return (abs(val+1) % 2)
    
class RemoveOddStrategy(FilterStrategy):

    def removeValue(self, val):
        return (abs(val) % 2)

class Values:
    def __init__(self, vals):
        self.vals = vals
    
    def filter(self, strategy):
        res = []
        for n in self.vals:
            if not strategy.removeValue(n):
                res.append(n)
        return res

# Usage
def demo():
    values = Values([-3, -2, -1, 0, 1, 2, 3])

    print(values.filter(RemoveNegativeStrategy()))
    print(values.filter(RemoveEvenStrategy()))
    print(values.filter(RemoveOddStrategy()))
