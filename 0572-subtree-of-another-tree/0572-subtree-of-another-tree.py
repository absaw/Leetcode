# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        elif (p and not q) or (not p and q):
            return False
        return (p.val==q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root,subRoot):
            return True
        
        left = self.isSubtree(root.left,subRoot) if root.left  else False
        right = self.isSubtree(root.right,subRoot) if root.right else False
        return left or right