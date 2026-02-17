# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # swap the right, and left child recursively using tuple unpacking
        root.left, root.right = root.right, root.left

        # recursively swap the child nodes
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root