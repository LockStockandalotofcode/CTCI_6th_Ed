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
        zigzag_flag = 1

        # make queue
        queue = deque([root])

        # BFS : level order traversal
        while queue:
            level_size = len(queue)
            temp_list = []

            for i in range(level_size):
                curr = queue.popleft()
                if i <= level_size - 1:
                    temp_list.append(curr.val)
                
                # push children to queue for next level
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            res.append(list(temp_list[::zigzag_flag]))
            zigzag_flag *= -1
        
        return res