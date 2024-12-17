# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            1  >  2 > 3 > 4
    prev   curr next
        
        '''

        prev = None
        curr = head
        
        while curr:
            #save next
            nxt = curr.next
            #link to prev
            curr.next = prev
            # move prev forward
            prev = curr
            # move curr forward
            curr = nxt
        
        return prev