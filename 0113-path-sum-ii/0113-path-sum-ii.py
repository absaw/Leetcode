# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''
        node = 11
        valList = [5,4,11,2]
        currSum = 22
        self.res = [[5,4,11,2]]
        '''
        self.res = []

        def dfs(node, valList,currSum):

            if not node:
                return
            valList.append(node.val)
            #valList = [5]
            currSum += node.val
            #currSum = 5

            if (not node.left and not node.right and currSum == targetSum):
                self.res.append(valList[:])
                valList.pop()
                return
            
            dfs(node.left, valList, currSum)
            dfs(node.right, valList, currSum)

            valList.pop()
        
        dfs(root,[],0)

        return self.res



