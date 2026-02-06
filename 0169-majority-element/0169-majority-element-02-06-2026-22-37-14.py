class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tracker = {}
        for num in nums:
            tracker[num] = tracker.get(num, 0) + 1

        major, max_count = 0, 0
        for num, count in tracker.items():
            if count > max_count:
                max_count = count
                major = num
        
        return major