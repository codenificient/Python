import random
class printQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
         self.pages.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None
        
    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    
    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

num = random.randint(0,11)

class Job:
    job = printQueue()
    pages = job.size()

    def print_page(self):
        if self.items:
            self.pages.dequeue()
            pages -= 1
            
    def check_complete(self):
        if self.pages.is_empty():
            return Done


class Printer:
       
    def get_job(self, pages):
        if printQueue.items.is_empty():
            check_complete()
        else:
            print_page()
