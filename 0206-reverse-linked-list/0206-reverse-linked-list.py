# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        1 > 2 > 3 > 4 > 5 > None
        pr cu  next
      N < 1 < 2 N
              p c  n  
        '''
        prev=None
        curr= head

        while curr:
            nxt = curr.next
            curr.next = prev
            #update for next iteration
            prev = curr
            curr = nxt
        return prev