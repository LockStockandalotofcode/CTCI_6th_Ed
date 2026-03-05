class Solution:
    def hammingWeight(self, n: int) -> int:
        # brian Kernighan's algorithm
        count = 0

        while n:
            n = (n & (n-1))
            count += 1
        
        return count