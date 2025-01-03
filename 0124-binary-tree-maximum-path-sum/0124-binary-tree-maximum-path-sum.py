# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            if not node:
                return 0
            nonlocal res
            leftMax = max(0,dfs(node.left))
            rightMax = max(0,dfs(node.right))

            currMax = node.val + leftMax + rightMax
            res = max(res, currMax)

            return node.val+max(leftMax,rightMax)
        dfs(root)
        return res
