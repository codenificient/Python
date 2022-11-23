class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)

    def get_data(self):
        """ Returns the self.data attribute """
        return self.data

    def set_data(self, new_data):
        """ Replaces the existing value of the self.data attribute with new_data parameter """
        self.data = new_data

    def get_next(self):
        """ Return the self.next attribute """
        return self.next

    def set_next(self, new_next):
        """ Replaces the existing self.next value with new_next parameter """
        self.next = new_next
