# Builder Pattern

class House:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def print(self):
        print(f"This {self.size} {self.color} house is amazing!")


class Treehouse(House):
    def __init__(self, size, color, tree_type):
        super().__init__(size, color)
        self.tree_type = tree_type

    def print(self):
        print(f"This {self.size} {self.color} treehouse on a {self.tree_type} tree is so cool!")


class Skyscraper:
    def __init__(self, height, material):
        self.height = height
        self.material = material

    def print(self):
        print(f"This {self.height}-meter tall skyscraper made of {self.material}.")


class HouseFactory:
    def createHouse(self, size, color):
        return House(size, color)

    def createTreehouse(self, size, color, tree_type):
        return Treehouse(size, color, tree_type)

    def createSkyscraper(self, height, material):
        return Skyscraper(height, material)

# Usage
def demo():
    houseFactory = HouseFactory()
    house = houseFactory.createHouse("medium", "blue")
    treehouse = houseFactory.createTreehouse("small", "green", "oak")
    skyscraper = houseFactory.createSkyscraper(300, "glass")

    house.print()
    treehouse.print()
    skyscraper.print()
