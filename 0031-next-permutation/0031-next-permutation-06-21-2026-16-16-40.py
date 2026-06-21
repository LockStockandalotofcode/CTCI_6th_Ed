class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        
        # find pivot : traversing right to left
            # point where increasing order breaks : number which is smaller than the number on its immediate right
            # one property: subarray to the right of this number is strictly decreasing
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        # find successor
        if i >= 0:
            s = n - 1
            while nums[s] <= nums[i]:
                s -= 1
                continue
            successor = nums[s]

            # swapping variables and not array elements
            # swap pivot and successor
            nums[s], nums[i] = nums[i], nums[s]

        # the tail, pivot to end is still decreasing, so to get the next permutation, reverse this tail, this also takes care of the case where we start with the largest lexicographical order
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        