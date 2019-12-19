class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self. next = None


class Deque:
    #initialize an empty deque
    def __init__(self):
        self.size = 0
        self.head = ListNode("head")#creating a dummy head 
        self.tail = ListNode("tail")#creating a dummy tail
        self.head.next = self.tail#pointing the head to the tail
        self.head.prev = self.head#pointing the tail to the head






    
    def isEmpty(self):


        return self.getSize() == 0


    def getSize(self):
        return self._size()






    def add_first(self, key, val):
        #head<-> tail
        #head<-> 1 <->tail
        #head<-> 2 <->1 <-> tail
        new_node = ListNode(item)
        prev_first = self.head.next 
        #update head.next.prev; creates pointer head<-1
        self.head.next.prev = new_node
        #update self.head.next; creates pointer head->
        self.head.next = new_node
        #update new nodes head and prev
        new_node.prev = self.head
        new_node.next = prev_first
        self.size += 1







    def add_last(self, key, val):
        #head <-> 1 <->tail
        #head <-> 1 <-> 2 <->tail

        new_node = ListNode(item)
        prev_last = self.tail.prev
        #update tail.next.prev; creates pointer 1<-tail
        self.tail.prev.next = new_node
        #update self.tail.next; 
        self.tail.prev = new_node
        




    

    def remove_first(self):





    def remove_last(self):



def asList(self):



    