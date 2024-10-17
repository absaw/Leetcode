# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k ==0 or not head:
            return head
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        
        k = k % n
        if k == 0:
            return head
        
        p1 = p2 = head
        ctr = 0
        while ctr <k:
            p2 = p2.next
            ctr += 1
     
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        
        res = p1.next
        p1.next = None
        p2.next = head

        return res
