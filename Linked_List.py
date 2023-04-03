class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data)

    def deleteValue(self, data):
        if not self.head:
            print('empty list')
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
            if not current.next:
                print('item not found in list')
                return

    def removeDuplicatesFromSorted(self):
        if not self.head:
            print('list is empty')
            return

        current = self.head

        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    def indexOf(self, data):
        if not self.head:
            print('list is empty')
            return

        current = self.head
        index = 0

        while current:
            if current.data == data:
                print(index)
                return
            current = current.next
            index += 1

        print(f'list does not contain {data}')
        return

    def removeDuplicatesFromUnsorted(self):
        if not self.head:
            print('empty list')
            return

        seen = {}
        prev = None
        current = self.head

        while current:
            if current.data in seen:
                prev.next = current.next
                current = current.next
            else:
                seen[current.data] = 1
                prev = current
                current = current.next

    # This one was a little tricky.
    def reverseList(self):
        if not self.head:
            print('cannot reverse empty list')
            return

        prev = None

    # This is essentially just walking the head/root along the list.
    # O(n) time complexity.
        while self.head:
            next_node = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = next_node

        self.head = prev

    def printList(self):
        if not self.head:
            print('empty list')
        else:
            current = self.head
            while current:
                print(current.data, end=' ')
                current = current.next