class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # BACKTRACKING

        p_str = ""
        res = []

        def backtrack(p_str: str, open_count: int, closed_count: int):

            nonlocal  res
            if len(p_str) == 2 * n:
                res.append(p_str)
                return 
            
            if open_count < n:
                backtrack(p_str + "(", open_count + 1, closed_count)

            if closed_count < open_count:
                backtrack(p_str + ")", open_count, closed_count + 1)
        
        backtrack("", 0, 0)
        return res