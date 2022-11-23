class Deque:
    """
    A deque is a double ended queue.
    """
    def __init__(self):
        self.items = []

    def add_front(self, item):
        """
        Takes an item as a parameter and inserts it into the 0th index of the list representing the Deque

        The runtime is linear, or O(n), because every time you insert into the front of a list, all the other items in the list need to shift one position to the right
        """

        self.items.insert(0, item)

    def add_rear(self, item):
        """
         Takes an item as a parameter and adds it to the end of the list representing the Deque

         The runtime is constant time, or O(1) because adding an item to the end of a list happens in constant time
        """
        self.items.append(item)

    def remove_front(self):
        """ if the list has items in it, this method will remove and return the item at the front of the list
        The runtime for this method is linear, O(n) because every time we remove an item at the front of the list, all the other items must move their position once to the left"""
        if self.items:
            return self.items.pop(0)
        return None


    def remove_rear(self):
        """
        Removes and returns the items at the end of the list representing this Deque
        """
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        if self.items == []:
            return 'This list is empty'
        return 'The list is not empty'
