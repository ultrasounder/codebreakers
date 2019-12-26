class ListNode:

    def __init__(self, key, val):
        self.val = val
        self.next = None
        self.prev = None
        


class Deque:
    #initialize an empty deque
    def __init__(self):
        self.size = 0
        self.head = ListNode("head")
        self.tail = ListNode("tail")
        self.head.next = self.tail
        self.tail.prev = self.head
    

    
    def isEmpty(self):


        return self.getSize() == 0


    def getSize(self):
        return self._size()






    def add_first(self, key, val):
        # head <-> tail
        # head <-> 1 <-> tail
        # head <-> 2 <-> 1 <-> tail
        new_node = ListNode(item)
        prev_first = self.head.next
        # update head.next.prev
        self.head.next.prev = new_node
        # update head.next
        self.head.next = new_node
        #update new nodes next and prev
        new_node.prev = self.head
        new_node.next = prev_first
        self.size += 1

        
        







    def add_last(self, key, val):
        
        




    

    def remove_first(self):





    def remove_last(self):



def asList(self):



    