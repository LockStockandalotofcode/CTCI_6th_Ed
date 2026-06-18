class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) # start with n index because last index goes upto n-1 only

        for i in range(len(nums)):
            res ^= nums[i] ^ i
        
        return res