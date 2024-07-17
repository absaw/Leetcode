# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []
        if not root:
            return result
        queue = deque()
        level = -1
        queue.append([root,0])

        while queue:

            node,node_level = queue.popleft()

            if node_level == level:
                result[node_level].append(node.val)
            else:
                level += 1
                result.append([node.val])
            
            for child in [node.left,node.right]:
                if child:
                    queue.append([child,level+1])
            
        
        return result




