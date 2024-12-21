# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
head 
1 > 2 > 3 > 4 > 5 > 6 > None
        m
1 > 6 > 2 > 5 > 3 > 4 > None

Find halfway point of list
set next to null
reverse 2nd linked list 
merge the the list alternately
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #halfway point
        dummy = ListNode()
        slow = head
        fast = head.next
        # dummy.next = slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # dummy = dummy.next
        head2 = slow.next
        slow.next = None
        #reverse a list
        # p > q > r
        prev= None
        curr = head2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # head2 = prev

        #merge them together
        curr1 = head
        curr2 = prev
        while curr2:
            nxt1 = curr1.next
            nxt2 = curr2.next
            curr1.next = curr2
            curr2.next = nxt1
            curr1 = nxt1
            curr2 = nxt2
        
        return head
            
