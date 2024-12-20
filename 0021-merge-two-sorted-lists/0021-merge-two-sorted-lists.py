# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy

        p = list1
        q = list2

        while p or q:
            val1 = p.val if p else float('inf')
            val2 = q.val if q else float('inf')
            if val1 < val2:
                nxt = p.next
                dummy.next = p
                p = nxt
            else:
                nxt = q.next
                dummy.next = q
                q = nxt
            dummy = dummy.next
        return head.next
