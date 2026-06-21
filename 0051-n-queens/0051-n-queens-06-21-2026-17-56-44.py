class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        # construct board with char of . and not string "...."
            # since strings in python are immutable
        board = [["."] * n for _ in range(n)]

        # defince sets to track unsafe positions as in unsafe columns, positive diags, and negative diags
        cols = set()
        pos_diags = set()
        neg_diags = set()

        # recursively backtrack over each row
        def backtrack(r: int):
            # BASE CASE: once all rows done, add to results list
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
                
            # place queen if safe
            for c in range(n):
                if c in cols or r + c in pos_diags or r - c in neg_diags:
                    continue       
                board[r][c] = "Q"             
                # mark positions unsafe, by its placement
                cols.add(c)
                pos_diags.add(r + c)
                neg_diags.add(r - c)
                
                # go down further, next row
                backtrack(r + 1)
                
                # backtrack to previous state, removing everything from memory
                board[r][c] = "."
                cols.remove(c)
                pos_diags.remove(r + c)
                neg_diags.remove(r - c)
                
        
        backtrack(0)
        return res