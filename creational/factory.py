# Factory Pattern


class House:
    def __init__(self, size: str, color: str):
        self.size = size
        self.color = color

    def print(self):
        print(f"This {self.size} {self.color} house is amazing!")


class Treehouse(House):
    def __init__(self, size: str, color: str, tree_type: str):
        super().__init__(size, color)
        self.tree_type = tree_type

    def print(self):
        print(f"This {self.size} {self.color} treehouse in the {self.tree_type} tree is so cool!")


class Skyscraper:
    def __init__(self, height: int, material: str):
        self.height = height
        self.material = material

    def print(self):
        print(f"This {self.height}-meter tall skyscraper is made of {self.material}.")


class HouseFactory:
    """Hides which class is created and with which arguments."""

    def create_small_house(self, color: str) -> House:
        return House("small", color)

    def create_medium_house(self, color: str) -> House:
        return House("medium", color)

    def create_large_house(self, color: str) -> House:
        return House("large", color)

    def create_oak_treehouse(self, color: str) -> Treehouse:
        return Treehouse("small", color, "oak")

    def create_pine_treehouse(self, color: str) -> Treehouse:
        return Treehouse("medium", color, "pine")

    def create_glass_skyscraper(self, height: int) -> Skyscraper:
        return Skyscraper(height, "glass")

    def create_steel_skyscraper(self, height: int) -> Skyscraper:
        return Skyscraper(height, "steel")


# Usage
def demo():
    house_factory = HouseFactory()
    house_factory.create_small_house("blue").print()
    house_factory.create_medium_house("red").print()
    house_factory.create_large_house("yellow").print()
    house_factory.create_oak_treehouse("brown").print()
    house_factory.create_pine_treehouse("green").print()
    house_factory.create_glass_skyscraper(300).print()
    house_factory.create_steel_skyscraper(500).print()
