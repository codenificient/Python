"""
Python Algorithms
Queue Class
"""
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.elements)


if __name__ == "__main__":
    lst = PriorityQueue()
    print(lst)
    print(lst.isEmpty())

    lst.put(43, 2)
    print(lst.isEmpty())
    lst.put(["hola", 23])
    print(lst.peek())

    print(lst)
    print(lst.get())