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
        # 1 > 2 > 3 > 4 > None
        #     s
        #              f   
        
        # 1 > 2 > 3 > 4 > 5
        
        # find the mid of list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_list = slow.next
        slow.next = None
        # reverse the second part list
        #    3>4>5>None
        # p  c nxt
        prev = None
        curr = second_list
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head2 = prev
        # merge the two lists
        # dummy
        #  1 > 2
        # ptr1
        # 4 > 3
        # ptr2
        dummy=ListNode()
        ptr1 = head
        ptr2 = head2
        dummy.next = ptr1
        while ptr1 and ptr2:
            ptr1nxt = ptr1.next
            ptr2nxt = ptr2.next

            ptr1.next= ptr2
            ptr2.next = ptr1nxt
            ptr1 = ptr1nxt
            ptr2 = ptr2nxt
        return dummy.next


        