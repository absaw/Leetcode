# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0

        def dfs(node,maxVal):
            nonlocal count
            if node.val >= maxVal:
                count += 1
                maxVal = max(node.val,maxVal)
            if node.left:
                dfs(node.left,maxVal)
            if node.right:
                dfs(node.right,maxVal)
        dfs(root,root.val)
        return count