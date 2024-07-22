# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        ll = []
        queue = collections.deque()
        curr_level = -1

        queue.append([root,curr_level+1])

        while queue:

            node, level = queue.popleft()

            if level == curr_level:
                ll.append(node.val)

            else:
                if ll:
                    res.append(ll[-1])
                ll = [node.val]
                curr_level += 1
            
            for neighbor in [node.left,node.right]:
                if neighbor:
                    queue.append([neighbor,level+1])
        res.append(ll[-1])
        
        return res


        

