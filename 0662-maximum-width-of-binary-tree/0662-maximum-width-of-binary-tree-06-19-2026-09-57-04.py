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
        
        queue = deque([(root, 1)])
        max_width = 0

        while queue:
            level_size = len(queue)

            # process level
            _, leftmost_node_idx = queue[0]
            _, rightmost_node_idx = queue[-1]
            
            # update max width; 
            # + 1 because 0-based indexing
            max_width = max(max_width, rightmost_node_idx - leftmost_node_idx + 1)

            # process all nodes in current level and push children nodes with apt indexing
            for _ in range(level_size):
                curr_node, curr_idx = queue.popleft()

                # push left child node with index 2i
                if curr_node.left:
                    queue.append((curr_node.left, 2 * curr_idx))
                # push right child node with index 2i + 1
                if curr_node.right:
                    queue.append((curr_node.right, 2 * curr_idx + 1))

        return max_width