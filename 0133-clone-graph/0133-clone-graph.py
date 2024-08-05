"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

        old_to_new = {}

        def get_node(node):
            if node in old_to_new:
                return old_to_new[node]
            if not node:
                return None
            new_node = Node(node.val,None)
            old_to_new[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(get_node(neighbor))
            
            return new_node
        
        return get_node(node) 