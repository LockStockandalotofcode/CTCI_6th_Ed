# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rank = 1

        # BST to map all node values to their rank
        def search(node: Optional[TreeNode]) -> int:
            nonlocal rank
            if not node:
                return None
            
            left_res = search(node.left)
            if left_res is not None:
                return left_res
            
            if rank == k:
                return node.val
            rank += 1

            return search(node.right)
            
        return search(root)