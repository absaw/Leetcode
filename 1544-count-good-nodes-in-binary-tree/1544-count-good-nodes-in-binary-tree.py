# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.result = 0

        def trav(root,max_value):

            if not root:
                return
            
            if root.val >= max_value:
                max_value = root.val
                self.result += 1
            
            trav(root.left,max_value)
            trav(root.right,max_value)
        
        trav(root,root.val)

        return self.result