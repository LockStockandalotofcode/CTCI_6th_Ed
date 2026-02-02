# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a "Dummy" node to handle edge cases (like removing the head)
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        
        # 2. Move 'fast' forward n steps
        for _ in range(n):
            fast = fast.next
            
        # 3. Move both until 'fast' reaches the very end
        while fast:
            slow = slow.next
            fast = fast.next
            
        # 4. Skip the Nth node
        slow.next = slow.next.next
        
        # Return the actual head (not the dummy)
        return dummy.next