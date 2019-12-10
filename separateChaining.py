class Node:
    def __init__(self, key, value):
        self. key = key
        self. value = value
        self.next = None

class separateChainingHashMap:
    #initialize HashMap

    def __init__(self, capacity):
        self.map = [Node("dummy") for _ in range(capacity)]
        

    #returns the index the key is stored

    def hashedIndex(self, key):
        return key % len(self.map)


    #adds an item to the hashmap
    def put(self, key, val):
        idx = hashedIndex(key)
        curr = self.map[idx]#chek to see if the key exists 
        while(curr.next):
            if curr.next.key == key:
                curr.next.val = val
                return
            curr = curr.next
        curr.next = Node(key, val)
            

    #finds items with given key and returns associated val
    def get(self, key):
        idx = hashedIndex(key)
        curr = self.map[idx]
        while(curr.next):
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return None

    
    #deletes a key and uts associated value
    def delete(self, key):
        idx = hashedIndex(key)
        prev = self.map[idx]#prev will be dummy node and curr will be dummy.next
        curr = prev.next
        while(curr):
            if curr.key == key:
                prev.next = curr.next
            prev = curr
            curr = curr.next



    #override toString method for debugging
    def __str__(self):
        


    if  __name__ == "__main__":
        pass




