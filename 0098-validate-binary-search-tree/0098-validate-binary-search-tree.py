# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check_BST(root,min_val,max_val):
            if not root:
                return True
        
            # current = True
            # if root.left:
            #     current = (root.left.val<max_val)
            # if root.right:
            #     current = current and (root.right.val>min_val)
            current = min_val < root.val < max_val
            left = check_BST(root.left,min_val,root.val)
            right = check_BST(root.right,root.val,max_val)
            
            return left and right and current
        
        return check_BST(root,-math.inf,math.inf)
        

