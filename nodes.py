class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
