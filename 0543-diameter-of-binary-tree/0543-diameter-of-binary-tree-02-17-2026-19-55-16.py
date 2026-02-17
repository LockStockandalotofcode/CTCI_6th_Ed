# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def get_height(node):
            if not node:
                return 0
            
            # recursively get heights of child nodes
            left_h = get_height(node.left)
            right_h = get_height(node.right)

            # update global maximum if diameter at this node is longer than the current max 
            self.max_diameter = max(self.max_diameter, left_h + right_h)

            # return height of this node to the parent node
            return 1 + max(left_h, right_h)
        
        get_height(root)
        return self.max_diameter
            