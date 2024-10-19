# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        path = set()
        def dfs(node, currSum, valList):

            if (not node or
                node in path ):
                return
            if (not node.left and not node.right and
                (currSum+node.val) == targetSum):
                # print(currSum)
                valList.append(node.val)
                self.res.append(valList.copy())
                valList.pop()
                return
            
            currSum += node.val
            valList.append(node.val)
            path.add(node)
            
            dfs(node.left, currSum, valList)
            dfs(node.right, currSum, valList)

            currSum -= node.val
            valList.pop()
            path.remove(node)
        dfs(root,0,[])
        # print(path)
        return self.res