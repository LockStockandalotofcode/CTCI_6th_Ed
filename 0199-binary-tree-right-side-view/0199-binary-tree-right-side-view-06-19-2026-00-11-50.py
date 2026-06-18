# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        
        # tweaking Preorder DFS (root -> right -> left)
        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return 
            
            # when reaching the first node at new depth level, it is 
            # rightmost node, because of our traversal style
            if depth == len(res):
                res.append(node.val)

            # Prioritise right child over left child one
            # to sync with traversal style
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res