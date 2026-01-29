from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use dict (equivalent of hashmap), since it is unordered
        seen = {}

        for n in nums:
            if n in seen:
                return True
            seen[n] = True

        return False

# Example usage:
# sol = Solution()
# print(sol.containsDuplicate([1,2,3,1]))