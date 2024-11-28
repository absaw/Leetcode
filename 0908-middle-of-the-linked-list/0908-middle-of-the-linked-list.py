# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1->2->3->4->5
            ^
      ^
1->2->3->4->5->6
                  ^
         ^
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast = slow = head
        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next
        
        return slow
