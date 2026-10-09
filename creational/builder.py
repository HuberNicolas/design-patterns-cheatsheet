# Builder Pattern


class House:
    def __init__(self):
        self.size = "medium"
        self.color = "white"
        self.floors = 1
        self.garage = False
        self.pool = False

    def print(self):
        extras = [name for name, has in (("a garage", self.garage), ("a pool", self.pool)) if has]
        with_extras = f" with {' and '.join(extras)}" if extras else ""
        print(f"This {self.size} {self.color} house has {self.floors} floor(s){with_extras}.")


class HouseBuilder:
    """Builds a House step by step; every step returns the builder so calls can be chained."""

    def __init__(self):
        self.house = House()

    def size(self, size: str) -> "HouseBuilder":
        self.house.size = size
        return self

    def color(self, color: str) -> "HouseBuilder":
        self.house.color = color
        return self

    def floors(self, floors: int) -> "HouseBuilder":
        self.house.floors = floors
        return self

    def with_garage(self) -> "HouseBuilder":
        self.house.garage = True
        return self

    def with_pool(self) -> "HouseBuilder":
        self.house.pool = True
        return self

    def build(self) -> House:
        house, self.house = self.house, House()  # reset, so the builder can be reused
        return house


class Architect:
    """Optional director: knows recipes for common houses."""

    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def family_house(self) -> House:
        return self.builder.size("large").floors(2).with_garage().build()

    def holiday_villa(self) -> House:
        return self.builder.color("yellow").with_pool().build()


# Usage
def demo():
    builder = HouseBuilder()
    builder.size("small").color("blue").build().print()
    builder.size("large").color("red").floors(3).with_garage().with_pool().build().print()

    architect = Architect(builder)
    architect.family_house().print()
    architect.holiday_villa().print()
