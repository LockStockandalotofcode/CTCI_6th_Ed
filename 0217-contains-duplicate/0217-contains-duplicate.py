class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use dict(equivalent of hashmap of java), since it is unordered
        seen = {}

        for n in nums:
            if n in seen:
                return True
            seen[n] = True

        return  False
