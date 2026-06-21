# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_global = -1000.0

        def dfs_helper(node: Optional[TreeNode]) -> int:
            nonlocal max_global
            if not node:
                return 0
            
            left_gain = max(dfs_helper(node.left), 0)
            right_gain = max(dfs_helper(node.right), 0)

            current_peak = node.val + left_gain + right_gain

            max_global = max(max_global, current_peak)

            return node.val + max(left_gain, right_gain)
        
        dfs_helper(root)
        return max_global