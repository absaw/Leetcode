# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
  p c>n
    1 2 3 4 5 N
  p<  c n
    1 2 3 4 5 N
save n=c.n 
c.n = p
p=c
c = n
n = n.n

'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head
        # nxt = head.next

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            # nxt = nxt.next
        return prev
