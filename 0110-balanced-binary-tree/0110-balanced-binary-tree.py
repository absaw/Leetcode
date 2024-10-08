# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def trav(root):

            if not root:
                return [True,0]
            
            left = trav(root.left)
            right = trav(root.right)
            balanced = left[0] and right[0] and \
                        (abs(left[1]-right[1])<=1)
            # print(balanced)
            return [balanced, 1+ max(left[1],right[1])]

        return trav(root)[0]