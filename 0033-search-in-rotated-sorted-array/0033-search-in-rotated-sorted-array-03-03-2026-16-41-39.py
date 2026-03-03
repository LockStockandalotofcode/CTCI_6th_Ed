class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if (nums[mid] == target):
                return mid

            # identify which half is sorted
            # Case 1: left half is sorted
            if nums[l] <= nums[mid]:
                # check if the target is in the left sorted range
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # Case 2: right half is sorted
            else:
                # check if the target is in the right sorted range
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
            