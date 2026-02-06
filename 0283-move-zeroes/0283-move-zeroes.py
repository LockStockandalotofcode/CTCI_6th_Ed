class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        current_freq = 0 # current frequency of zeroes
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                current_freq += 1
            else:
                nums[i - current_freq] = nums[i]
        
        for i in range(n-current_freq, n):
            nums[i] = 0