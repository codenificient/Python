class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
         """insert new item at index 0. runtime is O(n)"""
         self.items.insert(0, item)

    def dequeue(self):
        """Removes and returns the last  item in the queue. runtime is O(n)"""
        if self.items:
            return self.items.pop()
        return None
        
    def peek(self):
        """Returns the item at the end of the list, which represents the front-most item in the queue. Runtime is O(n)"""
        if self.items:
            return self.items[-1]
        return None

    
    def size(self):
        return len(self.items)
        """Returns the length of the list representign our queue. runtime is O(1) or constant time
        """



    def is_empty(self):
        """Returns a boolean value affirming whether or not our queue is empty. runtime is O(1) or constant time"""
        return self.items == []
