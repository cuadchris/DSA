class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    # helper method
    def _insert(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = Node(data)
            else:
                self._insert(node.left, data)

        elif data > node.data:
            if not node.right:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

        else:
            print('No duplicates allowed in tree')


tree = BinaryTree()
tree.insert(8)
tree.insert(9)
tree.insert(4)
tree.insert(2)
tree.insert(10)
print(tree.root.data)
print(tree.root.left.data)
print(tree.root.left.left.data)
print(tree.root.right.data)
print(tree.root.right.right.data)
