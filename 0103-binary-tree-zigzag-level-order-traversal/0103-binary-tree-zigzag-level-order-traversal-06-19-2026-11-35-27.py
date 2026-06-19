# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        # traversal flag: 
        # 1 for left to right
        # -1 for right to left
        left_to_right = True

        # make queue
        queue = deque([root])

        # BFS : level order traversal
        while queue:
            level_size = len(queue)
            level_list = deque()

            for i in range(level_size):
                curr = queue.popleft()
                if left_to_right:
                    level_list.append(curr.val)
                else:
                    level_list.appendleft(curr.val)
                
                # push children to queue for next level
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            res.append(list(level_list))
            left_to_right = not left_to_right
        
        return res