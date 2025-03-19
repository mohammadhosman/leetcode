# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_ll = []
        l1_curr = l1
        l2_curr= l2
        remainder = 0
        new_node_pointer = None
        prev_node_pointer = None
        while l1_curr is not None or l2_curr is not None or remainder != 0:
            l1_val = 0
            l2_val = 0
            if l1_curr is not None:
                l1_val = l1_curr.val
                l1_curr = l1_curr.next
            if l2_curr is not None:
                l2_val = l2_curr.val
                l2_curr = l2_curr.next
            new_node = ListNode(val=((l1_val + l2_val + remainder) % 10), next=None)
            prev_node_pointer = new_node_pointer
            new_node_pointer = new_node
            if prev_node_pointer is not None:
                prev_node_pointer.next = new_node
            remainder = int((l1_val + l2_val + remainder) / 10)
            new_ll.append(new_node)
        return new_ll[0]