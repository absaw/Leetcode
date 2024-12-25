"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummy = ListNode()

        curr_output = dummy
        curr = head
        node_map={}
        while curr:
            # create node
            newNode = None
            if curr in node_map:
                newNode = node_map[curr]
            else:
                newNode = ListNode(curr.val)
                node_map[curr] = newNode
            #random node
            curr_random = curr.random
            if curr_random in node_map:
                newNode.random = node_map[curr_random]
            else:
                if curr_random:
                    newNode.random = ListNode(curr_random.val)
                    node_map[curr_random] = newNode.random
                else:
                    newNode.random = None
            curr_output.next = newNode
            curr = curr.next
            curr_output = curr_output.next
        return dummy.next

            

