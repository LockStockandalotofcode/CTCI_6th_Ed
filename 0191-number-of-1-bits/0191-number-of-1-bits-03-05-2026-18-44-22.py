class Solution:
    def hammingWeight(self, n: int) -> int:
        # Bit shifting
        count = 0

        while n:
            count += (n & 1)
            n >>= 1
        
        return count