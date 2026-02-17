class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # sr - starting row, sc - starting column
        # Recursive DFS
        rows, cols = len(image), len(image[0])
        starting_color = image[sr][sc]

        if starting_color == color:
            return image

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != starting_color:
                return 
            
            image[r][c] = color

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        dfs(sr, sc)
        return image