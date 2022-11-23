"""
Python Algorithms
Two dimensional List
"""
class TwoDList:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return  not self.items

    def push(self, item):
        self.items.append(item)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    lst = TwoDList()
    print(lst)
    print(lst.isEmpty())

    lst.push(43)
    print(lst.isEmpty())
    lst.push(["hola", 23])
    print(lst)
