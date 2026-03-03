class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0

        # 1. initialise queue with all rotten oranges, and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
          # if zero fresh oranges at beginning, return 0
        if fresh == 0:
            return 0

        # 2. Multi-source BFS
        # process the queue
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while queue and fresh > 0 :
            minutes += 1
            # process all oranges currently in the queue(i.e. currently rotten)
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # if within bounds and orange is fresh
                    if (0<= nr < rows and 0<= nc < cols and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            
        
        return minutes if fresh == 0 else -1