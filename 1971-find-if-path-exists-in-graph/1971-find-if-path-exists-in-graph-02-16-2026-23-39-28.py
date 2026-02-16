class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # edge case 
        if source == destination:
            return True

        # adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS setup
        queue = deque([source])
        visited = {source} # set for easy lookup property

        # Traverse
        while queue:
            curr = queue.popleft()

            if curr == destination: 
                return True
            
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False