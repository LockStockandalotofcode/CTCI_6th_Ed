# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # recursive solution
        if not root:
            return True

        def isMirror(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2 or n1.val != n2.val:
                return False
            
            # compare inner and outer node pairs 
            return isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)
        
        return isMirror(root.left, root.right)