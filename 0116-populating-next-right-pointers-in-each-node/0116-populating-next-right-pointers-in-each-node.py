"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        # level order traversal
        # add root to deque
        # while not queue
        # popleft from queue to node
        # if queue is empty set right to none
        # else set next to first element in queue if in same level. if not same level set to none
        # add children to queue with level+1
        if not root:
            return None
        head = root
        queue = deque()
        level = 0
        queue.append([root,level])
        while(queue):
            node, level = queue.popleft()

            # if not queue:
            #     node.right = None #not needed
            # else:
            if queue:
                nextElement,nextLevel = queue[0]
                if nextLevel == level:
                    node.next = nextElement
            for child in [node.left,node.right]:
                if child:
                    queue.append([child,level+1])
        
        return head
                