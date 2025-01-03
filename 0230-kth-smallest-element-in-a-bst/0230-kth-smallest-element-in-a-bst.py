# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        count, res = k, root.val
        def inOrder(curr):
            nonlocal count, res
            if not curr:
                return
            inOrder(curr.left)
            count -= 1
            if count == 0:
                res = curr.val
                return
            inOrder(curr.right)
        inOrder(root)
        return res

