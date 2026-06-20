# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        
        # STEP 1 - Preparing hashmap by DFS
        parent_map = {} # hash map for node -> parent
        
        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode]):
            nonlocal parent_map
            if not node: 
                return 
            
            parent_map[node] = parent
            
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)

        # STEP 2 - BFS starting from the target node
        queue = deque([(target, 0)]) #queue containing list of tuples of current_node, distance_from_target_node
        visited = {target}
        res = []

        while queue:
            node, dist = queue.popleft()

            # If we've reached the target distance, append to result list
            if dist == k:
                res.append(node.val)
                continue # since, we want exact distance not greater than, dont need t ogo further

            neighbors = [node.left, node.right, parent_map.get(node, None)]

            for neighbor in neighbors:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return res