"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #create a copy of the whole list first
        if not head:
            return None
        node_map = {}
        curr = head

        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        #assign the random and next pointers
        while curr:
            if curr.next:
                node_map[curr].next = node_map[curr.next]
            if curr.random:
                node_map[curr].random = node_map[curr.random]
            curr = curr.next
        return node_map[head]