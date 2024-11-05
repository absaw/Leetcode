# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        def maxPath(root):
             
            if not root:
                return 0

            leftPathSum = maxPath(root.left)
            leftPathSum = leftPathSum if leftPathSum>=0 else 0
            rightPathSum = maxPath(root.right)
            rightPathSum = rightPathSum if rightPathSum>=0 else 0

            currentSum = leftPathSum + root.val + rightPathSum

            self.res = max(currentSum,self.res)

            return max(root.val+leftPathSum,root.val+rightPathSum)
        maxPath(root)
        return self.res