class Stack:

    def __init__(self):
        self ._items = []#creating an empty list to hold the items. _makes it a private variable 
    
    def is_empty(self):
        return not bool(self ._items)
    
    def size(self):
        return size(self ._items)
    
    def push(self, item):
        self ._items.append(item)

    def pop(self):
        return self ._items.pop()


        