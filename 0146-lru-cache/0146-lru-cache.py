'''
None <left > node1 > node2 >node3 > right > None
           <       <       <      <
left > right
     <
node_dict = {
    node1: #1
    node2:#2
    node3:#3
}
 '''
class Node:
    def __init__(self,key = 0,val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.node_dict = {}
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next=self.right
        self.right.prev = self.left
        self.nElements = 0
    def append(self,newNode):
        # node > right
        #      <
        # node > newNode > right
        #      <         <
        prev  = self.right.prev
        nxt = self.right
    
        newNode.next = nxt
        newNode.prev = prev
        prev.next = newNode
        nxt.prev = newNode
    
    def remove(self,node):
        nn = node.next
        pn = node.prev
        pn.next = nn
        nn.prev = pn
    
    def get(self, key: int) -> int:
        if key in self.node_dict:
            node = self.node_dict[key]
            # remove node from this position
            self.remove(node)
            # append node to end of the list
            self.append(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_dict:
            node = self.node_dict[key]
            #update value
            node.val = value
            # remove node from middle of list
            self.remove(node)
            # append node at end of the list
            self.append(node)
        else:
            # append node at end of the list
            node = Node(key,value)
            self.node_dict[key] = node
            # increase nElements
            if len(self.node_dict)>self.capacity:
                # remove left element
                # self.nElements-=1
                lastNode = self.left.next
                self.remove(lastNode)
                del self.node_dict[lastNode.key]
            # self.nElements += 1
            self.append(node)
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)