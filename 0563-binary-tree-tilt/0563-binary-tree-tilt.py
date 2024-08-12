# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def t_sum(node):
            if not node:
                return 0
            
            return node.val + t_sum(node.left) + t_sum(node.right)

        
        def calc(node):
            if not node:
                return 0
            ls = t_sum(node.left)
            rs = t_sum(node.right)

            return calc(node.left) + calc(node.right) + abs(ls-rs)
        
        return calc(root)

        