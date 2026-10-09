# Strategy Pattern

from abc import ABC, abstractmethod
from collections.abc import Callable


class FilterStrategy(ABC):
    @abstractmethod
    def remove_value(self, val: int) -> bool: ...


class RemoveNegativeStrategy(FilterStrategy):
    def remove_value(self, val: int) -> bool:
        return val < 0


class RemoveEvenStrategy(FilterStrategy):
    def remove_value(self, val: int) -> bool:
        return val % 2 == 0


class RemoveOddStrategy(FilterStrategy):
    def remove_value(self, val: int) -> bool:
        return val % 2 != 0


class Values:
    def __init__(self, vals: list[int]):
        self.vals = vals

    def filter(self, strategy: FilterStrategy) -> list[int]:
        return [n for n in self.vals if not strategy.remove_value(n)]

    # In Python, a plain function is often enough as a strategy.
    def filter_with(self, remove_value: Callable[[int], bool]) -> list[int]:
        return [n for n in self.vals if not remove_value(n)]


# Usage
def demo():
    values = Values([-3, -2, -1, 0, 1, 2, 3])

    print(values.filter(RemoveNegativeStrategy()))  # Output: [0, 1, 2, 3]
    print(values.filter(RemoveEvenStrategy()))  # Output: [-3, -1, 1, 3]
    print(values.filter(RemoveOddStrategy()))  # Output: [-2, 0, 2]
    print(values.filter_with(lambda n: abs(n) > 1))  # Output: [-1, 0, 1]
