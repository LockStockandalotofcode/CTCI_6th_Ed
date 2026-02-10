# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Move fast by 2 steps, and slow by 1 step
        # We check fast and fast.next to prevent AttributeError
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
            
        return False