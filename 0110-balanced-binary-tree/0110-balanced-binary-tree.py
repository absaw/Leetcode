# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        def checkHeight(root):

            if not root:
                return -1
            if not root.left and not root.right:
                return 0
            ld = 1+checkHeight(root.left)
            rd = 1+checkHeight(root.right)

            if abs(ld-rd)>1:
                self.result = False
            return max(ld,rd)
        checkHeight(root)
        return self.result
                
