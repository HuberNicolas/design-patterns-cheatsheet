# Iterator Pattern

from collections.abc import Iterator


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BinaryTreeIterator:
    """Classic iterator: keeps its own state and implements the iterator protocol."""

    def __init__(self, root: TreeNode | None):
        self.current = root
        self.stack: list[TreeNode] = []

    def __iter__(self) -> "BinaryTreeIterator":
        return self

    # inorder traversal
    def __next__(self) -> int:
        while self.current or self.stack:
            if self.current:
                self.stack.append(self.current)
                self.current = self.current.left
            else:
                node = self.stack.pop()
                self.current = node.right
                return node.val
        raise StopIteration


def inorder(node: TreeNode | None) -> Iterator[int]:
    """Pythonic iterator: a generator keeps the state for us."""
    if node:
        yield from inorder(node.left)
        yield node.val
        yield from inorder(node.right)


def build_tree() -> TreeNode:
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


# Usage
def demo():
    root = build_tree()

    print(list(BinaryTreeIterator(root)))  # Output: [4, 2, 5, 1, 6, 3, 7]
    print(list(inorder(root)))  # Output: [4, 2, 5, 1, 6, 3, 7]
