# Decorator Pattern

from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def get_description(self) -> str: ...

    @abstractmethod
    def get_cost(self) -> float: ...


class BasicCoffee(Coffee):
    def get_description(self) -> str:
        return "Coffee"

    def get_cost(self) -> float:
        return 2.0


class CoffeeDecorator(Coffee):
    """Wraps a coffee and has the same interface, so decorators can be stacked."""

    def __init__(self, coffee: Coffee):
        self.coffee = coffee

    def get_description(self) -> str:
        return self.coffee.get_description()

    def get_cost(self) -> float:
        return self.coffee.get_cost()


class MilkCoffeeDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return f"{self.coffee.get_description()}, Milk"

    def get_cost(self) -> float:
        return self.coffee.get_cost() + 0.5


class SugarCoffeeDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return f"{self.coffee.get_description()}, Sugar"

    def get_cost(self) -> float:
        return self.coffee.get_cost() + 0.3


class SweetFoamCoffeeDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return f"{self.coffee.get_description()}, Sweet Foam"

    def get_cost(self) -> float:
        return self.coffee.get_cost() + 0.7


# Usage
def demo():
    coffee = BasicCoffee()
    print(f"{coffee.get_description()}: {coffee.get_cost():.2f}")  # Output: Coffee: 2.00

    coffee = MilkCoffeeDecorator(coffee)
    print(f"{coffee.get_description()}: {coffee.get_cost():.2f}")  # Output: Coffee, Milk: 2.50

    coffee = SugarCoffeeDecorator(coffee)
    print(f"{coffee.get_description()}: {coffee.get_cost():.2f}")  # Output: Coffee, Milk, Sugar: 2.80

    coffee = SweetFoamCoffeeDecorator(coffee)
    print(f"{coffee.get_description()}: {coffee.get_cost():.2f}")  # Output: Coffee, Milk, Sugar, Sweet Foam: 3.50
