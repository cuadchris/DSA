class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    # ideally, these 2 methods would be on the tree itself. Will come back to this.
    def find_max(self):
        if not self.right:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if not self.left:
            return self.data
        return self.left.find_min()


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
