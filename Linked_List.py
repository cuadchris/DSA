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
        if self.head == None:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data)

    def deleteValue(self, data):
        if self.head == None:
            print('empty list')
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next != None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
            if not current.next:
                print('item not found in list')
                return

    def printList(self):
        if self.head == None:
            print('empty list')
        else:
            current = self.head
            while current:
                print(current.data, end=' ')
                current = current.next

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.deleteValue(2)
ll.deleteValue(22)
ll.prepend(25)
ll.printList()
