LRU Cache

get
# 1. return our correct hashmap value
# 2. update how we keep track of most recently seen query


put
# 1. set hashmap value
# 2. set this value as most recently seen
# 3. if this pushes us over capacity, we need to delete element used longest ago ( least recently)

Data structures:
hashmap: 4, 5, 3, 6
									more recent													least recent (haven't gotten or put in a long time)
doubly linked LL: head          6 -> 4 -> 3           tail

put(4)
put(5)
put(3)
get(4)
put(6)

capacity at 3




class LRUCache:

    def __init__(self, capacity: int):
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)