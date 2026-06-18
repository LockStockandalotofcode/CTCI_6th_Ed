class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2

        nums_sum = sum(nums)

        target = total - nums_sum
        return target