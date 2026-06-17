class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, total):
            # base case 1
            if total == target:
                res.append(list(cur))
                return
            # base case 2
            if total > target or i >= len(candidates):
                return
            
            # decision case 1 INCLUDE
            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])

            # Backtrack step: revert back to earlier state; before nect decision
            cur.pop()

            # decisions case 2 EXCLUDE
            backtrack(i+1, cur, total)


        backtrack(0, [], 0)
        return res
        