class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Swap Method

        current_freq = 0
        n = len(nums)

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[i - current_freq] = nums[i - current_freq], nums[i]
            else:
                current_freq += 1