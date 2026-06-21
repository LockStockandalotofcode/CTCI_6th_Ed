class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        # maintaining track of queen positions 
        # index of array is row number, val is the column
        queen_pos = [0] * n
        
        # defince sets to track unsafe positions as in unsafe columns, positive diags, and negative diags
        cols = set()
        pos_diags = set()
        neg_diags = set()

        # recursively backtrack over each row
        def backtrack(r: int):
            # BASE CASE: once all rows done, add to results list
            if r == n:
                board = []
                # generate string dynamically from tracking array
                for row_idx in range(n):
                    q_col = queen_pos[row_idx]
                    row_string = "." * q_col + "Q" + "." * (n - q_col - 1)
                    board.append(row_string)
                res.append(board)
                return
                
            # place queen if safe
            for c in range(n):
                if c in cols or r + c in pos_diags or r - c in neg_diags:
                    continue       
                queen_pos[r] = c             
                # mark positions unsafe, by its placement
                cols.add(c)
                pos_diags.add(r + c)
                neg_diags.add(r - c)
                
                # go down further, next row
                backtrack(r + 1)
                
                # backtrack to previous state, removing everything from memory
                queen_pos[r] = 0
                cols.remove(c)
                pos_diags.remove(r + c)
                neg_diags.remove(r - c)
                
        
        backtrack(0)
        return res