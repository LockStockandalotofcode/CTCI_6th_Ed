# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Overwrite current node's value  with next node's value
        node.val = node.next.val
        
        # Skip the next node
        node.next = node.next.next
        