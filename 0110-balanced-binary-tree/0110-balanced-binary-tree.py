# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def calculateHeight(root):

            if not root:
                return [-1,True]
            leftDepth,leftIsBalanced= calculateHeight(root.left)
            rightDepth,rightIsBalanced = calculateHeight(root.right)
            leftDepth +=1 
            rightDepth +=1
            if (not leftIsBalanced or not rightIsBalanced) or abs(leftDepth-rightDepth)>1:
                return [-1,False]
                
            return [max(leftDepth,rightDepth),True]
        # print(calculateHeight(root))
        return False if calculateHeight(root)[1]==False else True