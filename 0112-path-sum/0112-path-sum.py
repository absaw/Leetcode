# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        path = set()
        def dfs(node, currSum):

            if (not node or
                node in path):
                return False
            if (not node.right and not node.left and
                (currSum + node.val == targetSum)):
                return True
            
            currSum += node.val
            path.add(node)
            res = dfs(node.left,currSum) or dfs(node.right,currSum)
            currSum -= node.val
            path.remove(node)
            return res
        
        return dfs(root,0)