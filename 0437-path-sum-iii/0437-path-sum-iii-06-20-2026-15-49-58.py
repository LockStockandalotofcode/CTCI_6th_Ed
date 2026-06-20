# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def countFrom(node: Optional[TreeNode], current_sum: int) -> int:
            if not node:
                return 0

            count = 0
            if node.val == current_sum:
                count += 1
            
            count += countFrom(node.left, current_sum - node.val)
            count += countFrom(node.right, current_sum - node.val)
            return count
        
        return countFrom(root, targetSum) + \
              self.pathSum(root.left, targetSum) + \
              self.pathSum(root.right, targetSum)