from Stack import Stack
from nodes import TreeNode
from _queue import Queue


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    # helper method
    def _insert(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = TreeNode(data)
            else:
                self._insert(node.left, data)

        elif data > node.data:
            if not node.right:
                node.right = TreeNode(data)
            else:
                self._insert(node.right, data)

        else:
            print('No duplicates allowed in tree')

    def traverse_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.pre_order(self.root, '').strip('-')
        elif traversal_type == 'inorder':
            return self.in_order(self.root, '').strip('-')
        elif traversal_type == 'postorder':
            return self.post_order(self.root, '').strip('-')
        elif traversal_type == 'levelorder':
            return self.level_order(self.root).strip('-')
        elif traversal_type == 'reverselevelorder':
            return self.reverse_level_order(self.root).strip('-')
        else:
            print('invalid traversal type')

    # pre-order traversal.
    # check if current node is null
    # display node data
    # recursively traverse left subtree with pre-order method
    # recursively traverse right subtree with pre-order method
    def pre_order(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.data)) + '-'
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal

    # check if current node is null
    # recursively traverse left subtree with in-order method
    # display node data
    # recursively traverse right subtree with in-order method
    def in_order(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal += (str(start.data)) + '-'
            traversal = self.in_order(start.right, traversal)
        return traversal

    # check if current node is null
    # recursively traverse left subtree with post-order method
    # recursively traverse right subtree with post-order method
    # display node data
    def post_order(self, start, traversal):
        """Left -> Right -> Root"""
        if start:
            traversal = self.post_order(start.left, traversal)
            traversal = self.post_order(start.right, traversal)
            traversal += (str(start.data)) + '-'
        return traversal

    def level_order(self, start):
        if not start:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ''

        while len(queue) > 0:
            traversal += str(queue.peek()) + '-'
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_level_order(self, start):
        if not start:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ''

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.data) + '-'

        return traversal

    def search(self, data):
        if self.root:
            found = self._search(self.root, data)
            if found:
                return True
            return False
        else:
            return

    # helper method
    def _search(self, node, data):
        if data > node.data and node.right:
            return self._search(node.right, data)
        if data < node.data and node.left:
            return self._search(node.left, data)
        if data == node.data:
            return True

    def size_recursive(self):
        if not self.root:
            return 0
        return 1 + self._size_recursive(self.root.left) + self._size_recursive(self.root.right)

    # helper method
    def _size_recursive(self, node):
        if not node:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

    def size_iterative(self):
        if not self.root:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1

        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)

        return size

    def height(self):
        if not self.root:
            return 0
        return self._height(self.root)

    # helper method
    def _height(self, node):
        if not node:
            return -1
        left = self._height(node.left)
        right = self._height(node.right)

        return 1 + max(left, right)


tree = BinaryTree()
tree.insert(8)
tree.insert(9)
tree.insert(4)
tree.insert(2)
tree.insert(10)
tree.insert(6)
print(tree.traverse_tree('reverselevelorder'))
