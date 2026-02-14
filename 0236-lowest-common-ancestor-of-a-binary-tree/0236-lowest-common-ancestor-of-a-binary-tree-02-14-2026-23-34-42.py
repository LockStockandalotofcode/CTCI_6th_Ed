# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left_child = self.lowestCommonAncestor(root.left, p, q)
        right_child = self.lowestCommonAncestor(root.right, p, q)

        if left_child and right_child:
            # left_child and right_child are in different subtrees of this node
            return root
        
        # otherwise return the non-null child
        # below is the ternary operator in python
        return left_child if left_child else right_child