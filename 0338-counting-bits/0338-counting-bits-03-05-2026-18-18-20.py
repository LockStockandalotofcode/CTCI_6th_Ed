class Solution:
    def countBits(self, n: int) -> List[int]:
        # method 1: right shift( Even/ Odd)
        dp = [0] * (n+1)

        for i in range(1, n+1):
            dp[i] = dp[i >> 1] + (i % 2)
        
        return dp