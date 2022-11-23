class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "DLLNode object: data={}".format(self.data)

    def get_data(self):
        """Return the self.data attribute."""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data
        parameter."""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next
        parameter."""
        self.next = new_next

    def get_previous(self):
        """Return the self.previous attribute"""
        return self.previous

    def set_previous(self, new_previous):
        """Replace the existing value of the self.previous attribute with
        new_previous parameter."""
        self.previous = new_previous

class DLL:

    def __init__(self):
       self.head = None


    def __repr__(self):
        return "<DLL object: head=>".format(self.head)

    
    def is_empty(self):
        return self.head is None

        def size(self):
        """ Traverses a Linked List and returns an integer value of the number of items in the List
        
        The time complexity of this method is O(n) because every node in the Linked List must be visited in order to compute the size of the Linked List"""
        
        size = 0

            if self.head is None:
                return 0
        
            current = self.head
            while current is not None:  # while there are still nodes left to count
                size += 1
                current = current.get_next()

            return size

        def search(self, data):
            if self.head is None:
                return "Linked List is empty, No Nodes to search"

            current = self.head
            while current is not None:
            # The node data matches what we're looking for
                if current.get_data() == data:
                    return True
            
            # if the node data does not match
                else:
                    current = current.get_next()
            
                return False

    def add_front(self, data):
        pass

    def remove(self, data):
        pass