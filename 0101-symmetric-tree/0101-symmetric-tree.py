# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def checkTree(node1, node2):
	
            if not node1 and not node2:
                return True
            elif node1 and node2:
                return ( node1.val == node2.val and
                        checkTree(node1.left,node2.right) and 
                        checkTree(node1.right,node2.left))
            else:
                return False

        return checkTree(root,root)