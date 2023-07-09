# Decorator Pattern

class Coffee:
    def get_description(self):
        pass

    def get_cost(self):
        pass

class BasicCoffee(Coffee):
    def get_description(self):
        return "Coffee"

    def get_cost(self):
        return 2.0

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def get_description(self):
        return self.coffee.get_description()

    def get_cost(self):
        return self.coffee.get_cost()

class MilkCoffeeDecorator(CoffeeDecorator):
    def get_description(self):
        return f"{self.coffee.get_description()}, Milk"

    def get_cost(self):
        return self.coffee.get_cost() + 0.5

class SugarCoffeeDecorator(CoffeeDecorator):
    def get_description(self):
        return f"{self.coffee.get_description()}, Sugar"

    def get_cost(self):
        return self.coffee.get_cost() + 0.3

class SweetFoamCoffeeDecorator(CoffeeDecorator):
    def get_description(self):
        return f"{self.coffee.get_description()}, Sweet Foam"

    def get_cost(self):
        return self.coffee.get_cost() + 0.7

# Usage
def demo():
    # Create a basic coffee
    basic_coffee = BasicCoffee()
    print(basic_coffee.get_description())  # Output: Coffee
    print(basic_coffee.get_cost())  # Output: 2.0

    # Decorate the basic coffee with milk
    milk_coffee = MilkCoffeeDecorator(basic_coffee)
    print(milk_coffee.get_description())  # Output: Coffee, Milk
    print(milk_coffee.get_cost())  # Output: 2.5

    # Decorate the milk coffee with sugar
    sugar_milk_coffee = SugarCoffeeDecorator(milk_coffee)
    print(sugar_milk_coffee.get_description())  # Output: Coffee, Milk, Sugar
    print(sugar_milk_coffee.get_cost())  # Output: 2.8

    # Decorate the sugar milk coffee with sweet foam
    sweet_foam_sugar_milk_coffee = SweetFoamCoffeeDecorator(sugar_milk_coffee)
    print(sweet_foam_sugar_milk_coffee.get_description())  # Output: Coffee, Milk, Sugar, Sweet Foam
    print(sweet_foam_sugar_milk_coffee.get_cost())  # Output: 3.5
