class Queue:
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.isEmpty():
            return self.items[-1].data

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)
