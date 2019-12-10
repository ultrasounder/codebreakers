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


        


    def getSize(self):






    def add_first(self, key, val):





    def add_last(self, key, val):



    

    def remove_first(self):





    def remove_last(self):



def asList(self):



    