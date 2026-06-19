# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        curr_path = []

        def dfs(node: Optional[TreeNode], remaining_sum: int):
            # base condition
            if not node:
                return

            # process current node
            curr_path.append(node.val)

            # condition to accept or reject current path
            if not node.left and not node.right and remaining_sum == node.val:
                res.append(list(curr_path))
            # process for children nodes
            else:
                dfs(node.left, remaining_sum - node.val)
                dfs(node.right, remaining_sum - node.val)
            # backtrack: remove last addition: go to last intersection point
            curr_path.pop()
          
        dfs(root, targetSum)
        return res