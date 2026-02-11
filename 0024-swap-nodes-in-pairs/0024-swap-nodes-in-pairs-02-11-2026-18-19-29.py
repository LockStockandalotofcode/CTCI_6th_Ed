# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        # Iterate as long as there's a pair to swap
        while prev.next and prev.next.next:
            # identify the nodes to swap
            first = prev.next
            second = prev.next.next

            # Actual swapping for a pair of nodes
            # point previous node to => next node
            prev.next = second
            # point first node to => next to next node
            first.next = second.next
            # point next node to => first node
            second.next = first

            # move prev forward two spots for the next pair
            prev = first

        return dummy.next