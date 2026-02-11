# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 

        # Find the middle
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None # to break the linked list half
        right = tmp
        
        # reverse the second list
        right = self.reverseList(right)

        # Merge the two halves
        self.mergeLists(left, right)
    
    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            # save next
            tmp = curr.next
            # reverse
            curr.next = prev
            # move prev
            prev = curr
            # move curr
            curr = tmp
        
        return prev

    def mergeLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # This is different from mergeTwoLists(this is for sorted lists)
        # here the lists are not sorted
        # This merges the nodes by interleaving the nodes one from each list 
        
        while list2: 
            # first = list1 and second = list2
            # SAve next nodes
            tmp1, tmp2 = list1.next, list2.next

            # Re-wire pointers

            # first points to second, and second to first's original next
            list1.next = list2
            list2.next = tmp1

            # Move first and second
            list1, list2 = tmp1, tmp2