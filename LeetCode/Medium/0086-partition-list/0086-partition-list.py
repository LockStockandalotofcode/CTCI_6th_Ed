# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 2 separate dummy lists to store the partitions
        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head

        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next
        
        # To avoid cycles
        after.next = None
        before.next = after_head.next
        return before_head.next