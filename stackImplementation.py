class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

class Stack:

    def __init__(self):
        self.firstItem = None
        self._size = 0


    def __str__(self):
        pass


    
    
    def push(self, item):
        old_firstItem = self.firstItem
        self.firstItem = Node(item)
        self.firstItem.next = old_firstItem
        self._size += 1
        

    
    
    
    
    def pop(self, item):
        pass

    
    
    
    
    def isEmpty(self, item):
        pass



    def size(self):
        pass




    
    