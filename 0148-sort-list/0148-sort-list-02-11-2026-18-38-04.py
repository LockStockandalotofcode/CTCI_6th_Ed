# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Split
        # Split the list into two halves
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None # to break the link
        right = tmp

        # Sort
        # Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)

        # Merge
        # Merge the two sorted lists 
        return self.mergeTwoLists(left, right)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node that acts as a placeholder for result list
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next