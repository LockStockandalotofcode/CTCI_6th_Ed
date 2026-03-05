# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Iterative solution
        if not root:
            return True
        
        queue = deque([(root.left, root.right)])

        while queue:
            left, right = queue.popleft()

            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            
            queue.append((left.right, right.left))
            queue.append((left.left, right.right))
        
        return True
            