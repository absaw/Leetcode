# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity

#     def get(self, key: int) -> int:
        

#     def put(self, key: int, value: int) -> None:
        
class LRUCache:

	def __init__(self,capacity:int):
		self.capacity = capacity
		self.cache = OrderedDict()

	def get(self, key:int) -> int:
		#function to return val of key if exists else -1
		#when an element is found, move it to end i.e. most recently used position
		
		if key in self.cache:
			self.cache.move_to_end(key)
			return self.cache[key]
		else:
			return -1

	def put(self,key, value):
		#function to update val of key if exists else insert into cache
		#insertion should happen at end 
		#when capacity is reached, popitem(last = False), FIFO order
		
		if key not in self.cache and len(self.cache) == self.capacity:
			self.cache.popitem(last = False)
		self.cache[key] = value
		self.cache.move_to_end(key)


# 2:6,1:2,

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)