"""
Python Algorithms
Queue Class
"""
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def isEmpty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    lst = Queue()
    print(lst)
    print(lst.isEmpty())

    lst.enqueue(43)
    print(lst.isEmpty())
    lst.enqueue(["hola", 23])
    print(lst.peek())

    print(lst)
    print(lst.dequeue())