# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        result = []
        level = 0
        queue.append([root,level])
        # result.append([root.val])
        # queue = 15,7
        # res = [[3],[9,20],[15,7]]
        while queue:
            element,el_level = queue.popleft()
            if el_level>=len(result):
                result.append([])
            result[el_level].append(element.val)
            #add neighbors to queue
            for neighbor in [element.left,element.right]:
                if neighbor:
                    queue.append([neighbor,el_level+1])
        return result
