# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Tortoise and hare algo works fine here
        slow = head
        fast = head

        # Move fast by 2 and slow by 1
        # checking both fast and fast.next to prevent AttributeError

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Slow is exactly at the middle
        return slow
