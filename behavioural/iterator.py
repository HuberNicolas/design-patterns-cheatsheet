# Iterator Pattern

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTreeIterator:
    def __init__(self, root):
        self.root = root
        self.stack = []

    def __iter__(self):
        return self

    # inorder traversal
    def __next__(self):
        while self.root or self.stack:
            if self.root:
                self.stack.append(self.root)
                self.root = self.root.left
            else:
                node = self.stack.pop()
                value = node.val
                self.root = node.right
                return value
        raise StopIteration

# Usage
def demo():
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Create the iterator for the binary tree
    iterator = BinaryTreeIterator(root)

    # Iterate through the binary tree
    for val in iterator:
        print(val)
