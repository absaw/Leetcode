# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        merging 2 lists
        better to have a dummy node at the beginning to represent the output node
        pick the smaller node at each iteration
        When one of the lists are done, just add the other list's node to the end and the 
        result is formed 
               op  
                  p1
    d - 1 - 2 - 4
    
        5 > 6 > 7
        p2
        '''
        dummy = ListNode()
        ptr_output = dummy
        ptr1 = list1
        ptr2 = list2

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                ptr_output.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr_output.next = ptr2
                ptr2 = ptr2.next
            ptr_output = ptr_output.next
        if not ptr1:
            ptr_output.next = ptr2
        else:
            ptr_output.next = ptr1
        
        return dummy.next