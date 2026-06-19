# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node: Optional[TreeNode], curr_path: List[int], curr_sum: int):
            # Base condition
            if not node:
                return
            # update args and use them 
            new_path = curr_path + [node.val]
            curr_sum += node.val

            # process node
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    res.append(new_path)
                return

            # recurse for children nodes
            dfs(node.left, new_path, curr_sum)
            dfs(node.right, new_path, curr_sum)
          
        dfs(root, [], 0)
        return res