# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if not head:
            return None
        
        #find mid

        p1 = p2 = head
        prev = None
    
        while p2 and p2.next:
            prev = p1
            p1 = p1.next
            p2 = p2.next.next
        mid = p1
        if prev:
            prev.next = None
        r = mid.next
        m_val = mid.val
        
        newHead = TreeNode(m_val)
        if head != mid:
            newHead.left = self.sortedListToBST(head)
        newHead.right = self.sortedListToBST(r)

        return newHead