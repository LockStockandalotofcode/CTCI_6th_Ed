# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sort_map = {}
        
        rank = 1
        # BST to map all node values to their rank
        def sort_bst(node: Optional[TreeNode]):
            nonlocal rank

            if not node:
                return

            if node.left:
                sort_bst(node.left)
            
            sort_map[rank] = node.val
            rank += 1

            if node.right:
                sort_bst(node.right)
            
        sort_bst(root)
            
        res = sort_map.get(k)
        return res