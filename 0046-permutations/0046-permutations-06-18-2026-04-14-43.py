class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur):
            # base condition : if current permutation has all numbers
            if len(cur) == len(nums):
                res.append(list(cur))
                return
            
            # decision : to place every possible number in permutation
            for num in nums:
                if num not in cur:
                    cur.append(num)
                    backtrack(cur)
                    cur.pop()

        backtrack([])
        return res