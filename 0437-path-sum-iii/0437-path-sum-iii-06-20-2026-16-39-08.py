# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = {0: 1} # hashing prefix sums with frequency
        # sum of 0 always exists for empty tree

        total_paths = 0
        def dfs(node: Optional[TreeNode], current_sum: int):
            nonlocal total_paths
            
            # base case 
            if not node:
                return 

            current_sum += node.val

            # check if previously a path existed with same prefix sum
            # precisely look for an ancestor node, with value = current_Sum - target_sum
            total_paths += prefix_sums.get(current_sum - targetSum, 0)

            # update prefix sums hashmap
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

            # recurse for child nodes
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            # backtrack: revert back to state as in previous intersection
            prefix_sums[current_sum] -= 1
        
        dfs(root, 0)
        return total_paths