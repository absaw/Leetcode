# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0
        def calculate(root):
	
            if not root:
                return -1
            
            leftH = 1 + calculate(root.left)
            rightH = 1 + calculate(root.right)

            currDiam = leftH + rightH
            
            self.max_d = max(currDiam, self.max_d)

            return max(leftH,rightH)

        calculate(root)

        return self.max_d
