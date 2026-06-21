class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        
        # find pivot
        pivot_idx = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot_idx = i
                break

        # find next largest number in right suffix or tail to the  right of pivot
        if pivot_idx != -1:
            for j in range(n-1, pivot_idx, -1):
                if nums[j] > nums[pivot_idx]:
                    nums[pivot_idx], nums[j] = nums[j], nums[pivot_idx]
                    break

        # reverse the suffix tail
        nums[pivot_idx + 1 : ] = reversed(nums[pivot_idx + 1 : ])