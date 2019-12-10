class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class separateChainingHashMap:
    #initialize hashmap. Array of linked lists to support chainng
    def __init__(self, capacity):
        self.map = [Node("dummy") for _ in range(capacity)]

    


    #hash function
    def hashedIndex(self, key):
        return key % len(self.map)



    #store a value associated 
    def put(self, key, val):
        idx = hashedIndex(key)#calculate the index of the array location based on the key
        curr = self.map[idx]# intialize the pointer to the current location in the node based on the index
        while(curr.next):#while there is a next element in the node
            if curr.next.key == key: # if you find the key
                curr.next.val = val #update that location with the val
                return#exit
            curr = curr.next#if key has not been found
        curr.next = Node(key,val)#create a new node object at the end of the linkedlist



    
    def get(self, key):
        idx = hashedIndex(key)
        curr = self.map[idx]
        while(curr.next):
            if curr.next.key == key:
                return curr.next.val
            curr= curr.next
        return



    def delete(self, key):
        idx = hashedIndex(key)
        prev = self.map[idx]
        curr = prev.next
        while(curr):
            if curr.key == key:
                prev.next = curr.next
            prev = curr
            curr = curr.next      
        

    def __str__(self):
        out = ""
        for idx in self.map:
            curr = self.map[idx]
            while(curr):
                out += str(curr.val)
                curr = curr.next
            out += "\n"
        return  out


if __name__ == "__main__":
    map = separateChainingHashMap(3)
    for i in range(10):
        map.put(i, i*2)
    print(map)
    print(map.)

    



        