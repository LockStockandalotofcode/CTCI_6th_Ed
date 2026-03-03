class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base case
        if not grid: 
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # Base case: out of bounds or hitting water/already visited 
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == "0"):
                return
            
            # sink the land 
            grid[r][c] = "0"

            # visit all 4  neighbors 
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        
        return islands