class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Offset method
        current_freq = 0 # current frequency of zeroes
        n = len(nums)
        # Phase 1: Shift non-zeros forward using the zero-count as an offset
        for i in range(n):
            if nums[i] == 0:
                current_freq += 1
            else:
                # If current_freq is 0, this just does nums[i] = nums[i]
                nums[i - current_freq] = nums[i]
        
        # Phase 2: Fill the remaining slots at the end with 0
        # We need to fill exactly 'current_freq' number of slots
        for i in range(n-current_freq, n):
            nums[i] = 0