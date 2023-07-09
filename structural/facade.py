# Facade Pattern

class Stack:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0, 0]

    def push(self, n):
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def pop(self):
        if self.length > 0:
            self.length -= 1
            return self.arr[self.length]

    def resize(self):
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr


class StackFacade:
    def __init__(self):
        self.stack = Stack()

    def push(self, item):
        self.stack.push(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return self.stack.length == 0

    def size(self):
        return self.stack.length


# Usage
def demo():
    stack_facade = StackFacade()
    stack_facade.push(10)
    stack_facade.push(20)
    stack_facade.push(30)

    print(stack_facade.pop())  # Output: 30
    print(stack_facade.size())  # Output: 2
    print(stack_facade.is_empty())  # Output: False
