LRU Cache

get
# 1. return our correct hashmap value
# 2. update how we keep track of most recently seen query


put
# 1. set hashmap value
# 2. set this value as most recently seen
# 3. if this pushes us over capacity, we need to delete element used longest ago ( least recently)

# Data structures:
# hashmap: 4, 5, 3, 6
# 									more recent													least recent (haven't gotten or put in a long time)
# doubly linked LL: head          6 -> 4 -> 3           tail

# put(4)
# put(5)
# put(3)
# get(4)
# put(6)

# capacity at 3




# class LRUCache:

#     def __init__(self, capacity: int):
        

#     def get(self, key: int) -> int:
        

#     def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
class Node:
    def __init__(self, key, val):
        self.prev = prev
        self.next = None
        self.val = val
        self.key = key

class DoublyLinkedList:
    def __init__(self, key, value):
        self.back = Node("back", "back")
        self.front = Node("front", "front")
        self.back.next = self.front
        self.front.prev = self.back

    def delete(self, node):
        node.prev.next = self.front
        node.next.prev = self.back

     
    def addToFront(self, key, val):
        newNode = Node(key,val)
        front.prev.next = newNode
        front.prev = newNode
        newNode.next = self.front
        newNode.prev = self.front.prev


    def deleteFromBack(self):
        key = self.back.next.key
        self.back.next = self.back.next.next
        return key


    





class LRU_Cache:
    def __init__(self, capacity):
        self. node = DoublyLinkedList()
        self.capacity = capacity
        #key, node obj
        self.inCache = {}

    def __str__(self):
        cur = self.back.next
        out = ""
        while(cur):
            out += cur.val
#if node exists then delete it and add it to the front and return the val
    def get(self, key, val):
        if key in self.inCache:
            self.nodes.delete(self.inCache[key])
            self.nodes.addToFront(key, val)
            return val
        return None

    #if Node doesnt exist then add it to front and kick if over capacity, otherwise 
    def set(self,key, value):
        if key in self.inCache:
            self.nodes.delete(self.inCache[key])
            self.nodes.addToFront(key, value)
        else:
            self.nodes.addToFront(key, value)
            self.countNodes += 1
            if self.countNodes > self.capacity:
                #also remove from inCache
                key = self.nodes.deleteFromBack()
                del self.inCache[key]
                self.countNodes -= 1

lru = LRU_Cache(3)
lru.set(1,1)
lru.set(2,2)
lru.set(3,3)