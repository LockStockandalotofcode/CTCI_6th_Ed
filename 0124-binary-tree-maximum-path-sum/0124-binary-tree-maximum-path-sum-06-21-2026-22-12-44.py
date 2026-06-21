# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # TO COMPLETELY AVOID STACK OVERFLOW CRASHES
        # STACK AND HASHMAP
        gains = {None: 0} # hashmap treeNode -> max gain from either subtree
        # keeps track of gains on each subtree
        # above initialisation to handle leaf nodes when their child is None Node, and gains{} is used to look up child nodes' gains
        max_global = float('-inf')
        stack = [root]

        visited = set()

        while(stack):
            node = stack[-1]
            if not node:
                stack.pop()
                continue

            if node not in visited:
                visited.add(node)
                stack.append(node.right)
                stack.append(node.left)
            else:
                stack.pop()
                left_gain = max(gains.get(node.left, 0), 0)
                right_gain = max(gains.get(node.right, 0), 0)
                current_peak = node.val + left_gain + right_gain
                max_global = max(max_global, current_peak)
                gains[node] = node.val + max(left_gain, right_gain)
        
        return max_global