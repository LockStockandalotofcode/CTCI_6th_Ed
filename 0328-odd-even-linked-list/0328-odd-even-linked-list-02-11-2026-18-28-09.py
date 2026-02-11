# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # create 2 separate chains for odd and even positions, and then stitch them together at the end(save head of first even node)
        odd = head
        even = head.next
        even_head = even

        # Traverse the list 
        # check even and even.next to continue swapping
        # checking even and not odd since even is always ahead of odd
        # checking even ensures we don't run off the end of the list, and checking even.next ensures there is another odd node available to jump to.
        while even and even.next:
            # make the current odd node the next odd node
            odd.next = even.next
            odd = odd.next

            # make the current even node the next even node 
            even.next = odd.next
            even = even.next
        
        # attach the even list to the end of the odd list
        odd.next = even_head

        return head