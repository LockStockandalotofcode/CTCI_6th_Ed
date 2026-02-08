class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        result = []

        for i in range(n):
            # Skip the same 'i' to avoid dupliacte triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right  = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate 'left' values
                    while left < right and nums[left] ==  nums[left - 1]:
                        left += 1
                    
        return result