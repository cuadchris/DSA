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

    def traverse_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_traversal(self.root, '').strip('-')
        elif traversal_type == 'inorder':
            return self.inorder_traversal(self.root, '').strip('-')
        elif traversal_type == 'postorder':
            return self.postorder_traversal(self.root, '').strip('-')
        else:
            print('invalid traversal type')

    # pre-order traversal.
    # check if current node is null
    # display node data
    # recursively traverse left subtree with pre-order method
    # recursively traverse right subtree with pre-order method
    def preorder_traversal(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.data) + '-')
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    # check if current node is null
    # recursively traverse left subtree with in-order method
    # display node data
    # recursively traverse right subtree with in-order method
    def inorder_traversal(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.data) + '-')
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    # check if current node is null
    # recursively traverse left subtree with post-order method
    # recursively traverse right subtree with post-order method
    # display node data
    def postorder_traversal(self, start, traversal):
        """Left -> Right -> Root"""
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.data) + '-')
        return traversal


tree = BinaryTree()
tree.insert(8)
tree.insert(9)
tree.insert(4)
tree.insert(2)
tree.insert(10)
tree.insert(6)
print(tree.traverse_tree('inorder'))  # 2-4-6-8-9-10
print(tree.traverse_tree('preorder'))  # 8-4-2-6-9-10
print(tree.traverse_tree('postorder'))  # 2-6-4-10-9-8
