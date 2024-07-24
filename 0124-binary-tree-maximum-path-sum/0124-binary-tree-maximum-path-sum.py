# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.result = root.val

        def binTree(root):

            if not root:
                return 0

            leftM = max(0,binTree(root.left))
            rightM = max(0,binTree(root.right))

            self.result = max(self.result,root.val + leftM + rightM)

            return max(0,root.val+leftM,root.val+rightM)

        binTree(root)

        return self.result
