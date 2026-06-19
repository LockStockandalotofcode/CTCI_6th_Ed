# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        stack = [(root, [root.val], targetSum - root.val)]

        while stack:
            node, path, rem_sum = stack.pop()

            if not node.left and not node.right and rem_sum == 0:
                res.append(list(path))
                
            if node.right:
                stack.append((node.right, path + [node.right.val], rem_sum - node.right.val))
            if node.left:
                stack.append((node.left, path + [node.left.val], rem_sum - node.left.val))


        return res