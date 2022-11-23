class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """ accepts an item as a parameter and appends it to the end of the list.
        Returns nothing.

        The runtime for this operation happens in constant time or O(n) (python)
        """
        self.items.append(item)

    def pop(self):
            """ This method removes and returns the last item for the list, which is also the top item of the stack
            The runtime for this operation happens in constant time or O(n) (python)
            """
            if self.items:
                return self.items.pop()
            return None

    def peek(self):
        """ This method returns the last item for the list, which is also the top item of the stack
            The runtime for this operation happens in constant time or O(n) (python)
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """ This method returns the last length of the list, that is representing the stack
            The runtime for this operation happens in constant time or O(n) (python)
        """
        return len(self.items)

    def is_empty(self):
"""
    this boolean returns a true or false value whether the stack is empty or not. the operation happens in constant time
"""

        return self.items == []