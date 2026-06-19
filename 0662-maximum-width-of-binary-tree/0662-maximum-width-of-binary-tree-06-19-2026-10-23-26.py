# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_width = 0

        # DFS - maintaining hashmap - (depth -> node_index)
        # node_index is positional index 
        leftmost_indices = {}
        # width calculated for every node, compareda and updated max-width

        def dfs(node: Optional[TreeNode], depth: int, node_index: int):
            nonlocal max_width
            if not node:
                return
            
            # if leftmost node, update hashmap for leftmost nodes
            if depth not in leftmost_indices:
                leftmost_indices[depth] = node_index
            
            curr_width = node_index - leftmost_indices[depth] + 1
            max_width = max(max_width, curr_width)

            # recursively call for children nodes
            if node.left:
                dfs(node.left, depth + 1, 2 * node_index)
            if node.right:
                dfs(node.right, depth + 1, 2 * node_index + 1)

        dfs(root, 0 ,1)
        return max_width