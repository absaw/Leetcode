# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        #reverse second:
        # 1 > 2 > 3 >None
        #   prev curr nxt
        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev

        #join the 2 lists
        #first > 1 > 2 > 3 > 4
        #second > 7 > 6 > 5 
        first = head 
        while second:
            tmp1 = first.next #3
            tmp2 = second.next #5
            first.next = second #1>7>2
            second.next = tmp1 #1>7>2>6>
            first = tmp1 #2 
            second = tmp2 #6
        return head