# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        max_depth = 0 
        depth = 0 

        def backtrack(start, depth) -> int:
            if start.left == None and start.right == None:
                return depth
            d1 = 0
            d2 = 0
            if start.left:
                d1 = depth + backtrack(start.left, 1)
            if start.right:
                d2 = depth + backtrack(start.right, 1)
            
            max_d = max(d1, d2, max_depth)
            return max_d
            

        max_depth = backtrack(root, 1)
        return max_depth
        
