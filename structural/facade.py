# Facade Pattern


class DynamicArray:
    """The 'complex subsystem': manages capacity and resizing by hand."""

    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * self.capacity

    def push_back(self, n: int):
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def pop_back(self) -> int | None:
        if self.length > 0:
            self.length -= 1
            return self.arr[self.length]
        return None

    def resize(self):
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr


class StackFacade:
    """A small, simple interface; callers never see capacity or resizing."""

    def __init__(self):
        self._array = DynamicArray()

    def push(self, item: int):
        self._array.push_back(item)

    def pop(self) -> int | None:
        return self._array.pop_back()

    def is_empty(self) -> bool:
        return self._array.length == 0

    def size(self) -> int:
        return self._array.length


# Usage
def demo():
    stack = StackFacade()
    stack.push(10)
    stack.push(20)
    stack.push(30)  # triggers a resize behind the facade

    print(stack.pop())  # Output: 30
    print(stack.size())  # Output: 2
    print(stack.is_empty())  # Output: False
