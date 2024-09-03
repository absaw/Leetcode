# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # if not root:
        #     return None
        # if not root.left and not root.right:
        #     return root
        
        # temp = self.flatten(root.right)

        # root.right = self.flatten(root.left)
        # root.left = None
        # while root.right != None:
        #     root = root.right
        
        # root.right = temp
        # root.left = None
        # return root
        if not root:
            return
        
        # Recursively flatten the left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Store the right subtree in a temporary variable
        temp_right = root.right
        
        # Move the flattened left subtree to the right
        root.right = root.left
        root.left = None
        
        # Traverse to the end of the new right subtree
        while root.right:
            root = root.right
        
        # Attach the flattened right subtree
        root.right = temp_right