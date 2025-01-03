# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)<1:
            return None

        rootVal = preorder[0]
        rootIdx = inorder.index(rootVal)
        leftIn = inorder[:rootIdx]
        rightIn = inorder[rootIdx+1:]
        leftPre = preorder[1:rootIdx+1]
        rightPre = preorder[rootIdx+1:]
        root = TreeNode(rootVal)
        root.left = self.buildTree(leftPre, leftIn)
        root.right = self.buildTree(rightPre, rightIn)
        return root