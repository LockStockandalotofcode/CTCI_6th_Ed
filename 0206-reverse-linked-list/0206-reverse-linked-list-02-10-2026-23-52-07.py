# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Pointer flipping approach
        prev = None
        curr = head

        while curr:
            # SAve the next node, so as to not lose this.
            nxt = curr.next

            # reverse the pointing arrow for this node
            curr.next = prev

            # move curr and prev node by one forward
            prev = curr
            curr = nxt

        return prev