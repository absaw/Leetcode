# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        # def find_LCA(root,p,q):
        # curr = root

        # while curr:
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        
        elif not left and right:
            return right

        elif not right and left:
            return left
        
