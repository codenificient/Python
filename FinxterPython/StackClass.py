class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)


    def size(self):
        return len(self.items)

    def isEmpty(self):
        return not self.items

    def pop(self):
        return self.items.pop()

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    myStack = Stack()

    myList = ["python", "is", "so", "cool"]

    for word in myList:
        myStack.push(word)

    print(myStack)
    print(myStack.pop())
    print(myStack)
    
