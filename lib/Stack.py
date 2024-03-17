class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit  # Checks if the stack is full based on the limit

    def empty(self):
        return len(self.items) == 0  # Checks if the stack is empty

    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - 1 - i
        return -1
