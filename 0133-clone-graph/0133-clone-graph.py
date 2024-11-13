"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

Create a dictionary which stores the cloned new nodes
Perform a dfs from the current node
When a new node is seen, create a clone and store
When its already seen, get it and append it to the neighbor
      v
1-2-3-4
| |\
5 6 7

1n 2n 3n-4n
1:1n
2:2n
3:3n
4: 4n
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeDict = {}
        def dfs(node):
            if node in nodeDict:
                return nodeDict[node]
            
            newNode = Node(node.val)
            nodeDict[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode

        return dfs(node) if node else None