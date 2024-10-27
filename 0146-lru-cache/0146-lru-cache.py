"""
double linked list - 
Node 
key: storing key
val: storing value 
left - store tail - least recent
right - store head - most recent
eviction policy: eliminate LRU node if len(cache)>capacity

hash map 
stores key, 
val: reference of the corresponding node in the double linked list
                          prev  newNode  next
None <- Node1-> Node2 -> Node3 ->        None
     ->      <-       <-       <-

    
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_map = {}
        self.head = Node(0,0) # Insert
        self.tail = Node(0,0) # Evict
        self.head.left = self.tail
        self.tail.right = self.head
        self.capacity = capacity
    
    def remove(self, key):
        # print(key)
        # print(self.cache_map)
        nodeToBeRemoved = self.cache_map[key]
        prev = nodeToBeRemoved.left
        nxt = nodeToBeRemoved.right
        prev.right, nxt.left = nxt, prev

    def insert(self,key):
        
        # newNode = Node(key,value)
        newNode=self.cache_map[key]
        prev = self.head.left 
        nxt = self.head
        prev.right = newNode
        nxt.left = newNode
        newNode.left = prev
        newNode.right = nxt

    def get(self, key: int) -> int:
        
        if key in self.cache_map:
            self.remove(key)
            self.insert(key)
            return self.cache_map[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache_map:
            self.remove(key)
            self.insert(key)
            self.cache_map[key].val = value
        else:
            self.cache_map[key] = Node(key,value)
            self.insert(key)
        
        if len(self.cache_map) > self.capacity:
            lru_node = self.tail.right
            self.remove(lru_node.key)
            del self.cache_map[lru_node.key]

        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)