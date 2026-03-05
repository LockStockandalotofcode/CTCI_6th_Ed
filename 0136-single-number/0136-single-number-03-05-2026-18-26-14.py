class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        # 3 properties of XOR very useful
        # identity, self-cancellation, commutative/associative

        for num in nums:
            result ^= num
        
        return result