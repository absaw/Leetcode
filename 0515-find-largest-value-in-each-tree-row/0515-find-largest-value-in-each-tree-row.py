# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()

        queue.append(root)
        result = []

        while queue:
            qLen = len(queue)
            maxVal = float('-inf')
            for _ in range(qLen):
                element = queue.popleft()
                if element.val > maxVal:
                    maxVal = element.val
                #add child to queue for next level iteration
                for child in [element.left,element.right]:
                    if child:
                        queue.append(child)
            
            result.append(maxVal)
        
        return result
        