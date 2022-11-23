class QueueClass:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    myQ = QueueClass()

    myList = ["queues", "are", "easy", "in", "python"]

    print(myQ.isEmpty())

    for word in myList:
        myQ.enqueue(word)

    print(myQ)

    print(myQ.dequeue())

    print(myQ)
