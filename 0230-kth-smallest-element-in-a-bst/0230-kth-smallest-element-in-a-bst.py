# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.count = 0
        self.result = None

        def trav(root):

            if not root or self.result:
                return
            
            trav(root.left)

            self.count += 1

            if self.count == k:
                self.result = root
                return
            
            trav(root.right)
        trav(root)
        return self.result.val

