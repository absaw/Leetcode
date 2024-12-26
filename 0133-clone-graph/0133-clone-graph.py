"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
node_dict = {
    old:new
    1o : 1n
    2o : 2n
    3o : 3n
}
1o:
    val = 1
    neighbors = [2o, 3o, 4o]
1n:
    val = 1
    neighbors = [2n, 3n, 4n]
traverse through the graph, in recursive manner: dfs
if node in dict: return node 
else
    add it to dict, for future use
    add the neighbors to dict

"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        self.node_dict = {}

        def get_clone(node):
            if not node:
                return
            if node in self.node_dict:
                return self.node_dict[node]
            
            newNode = Node(node.val)
            self.node_dict[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(get_clone(neighbor))
            
            return newNode
        return get_clone(node) if node else None