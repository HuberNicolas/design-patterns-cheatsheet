# Facoty Pattern

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
    def createSmallHouse(self, color):
        size = "small"
        return House(size, color)

    def createMediumHouse(self, color):
        size = "medium"
        return House(size, color)

    def createLargeHouse(self, color):
        size = "large"
        return House(size, color)

    def createOakTreehouse(self, color):
        size = "small"
        tree_type = "oak"
        return Treehouse(size, color, tree_type)

    def createPineTreehouse(self, color):
        size = "medium"
        tree_type = "pine"
        return Treehouse(size, color, tree_type)

    def createGlassSkyscraper(self, height):
        material = "glass"
        return Skyscraper(height, material)

    def createSteelSkyscraper(self, height):
        material = "steel"
        return Skyscraper(height, material)

# Usage
def demo():
    houseFactory = HouseFactory()
    houseFactory.createSmallHouse("blue").print()
    houseFactory.createMediumHouse("red").print()
    houseFactory.createLargeHouse("yellow").print()
    houseFactory.createOakTreehouse("brown").print()
    houseFactory.createPineTreehouse("green").print()
    houseFactory.createGlassSkyscraper(300).print()
    houseFactory.createSteelSkyscraper(500).print()
