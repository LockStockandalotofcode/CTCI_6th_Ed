class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # BRUTE FORCE WAY
        res = [[]]

        # 2 choices for every number
        # covers all subsets
        for num in nums:
            curr_size = len(res)

            for i in range(curr_size):
                new_subset = res[i] + [num]
                res.append(new_subset)
        
        return res