# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0

        if not root:
            return 0

        def maxDepth(root):

            if not root:
                return -1
            # if not root.right and not root.left:
            #     return 0
            ld = 1+maxDepth(root.left)
            rd = 1+maxDepth(root.right)
            self.diameter = max(self.diameter,ld+rd)
            return max(ld,rd)
        maxDepth(root)
        return self.diameter