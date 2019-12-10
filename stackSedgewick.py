class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    #Initialize Stack
    def __init__(self):
        self.first_item = None
        self._size = 0
    #Method to iterate thorugh the stack and print all the items
    def __str__(self):
        curr = self.first_item#set pointer to current location
        out = ""#create a string object
        while(curr):#while the current pointer is not a null(end of the stack)
            out += str(curr.val) + '|'#concatenate the current value to the output string
            curr = curr.next#update the pointer to the next node location
        return out

    def push(self, item):
        old_first_item = self.first_item
        self.first_item = Node(item)
        self.first_item.next = old_first_item
        self._size += 1


    def pop(self):
        old_first_item = self.first_item



    def isEmpty(self):
        return self.size() == 0
    
    def size(self, item):
        return self._size

    


    

