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
        queue = deque([root])

        while queue:
            level_size = len(queue)

            # Iterate through all nodes at current level
            for i in range(level_size):
                curr = queue.popleft()

                # add last element at current level, that is the rightmost element
                if i == level_size - 1:
                    res.append(curr.val)
                
                # Push childen to queue for next level
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return res