from math import comb

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def solve(arr):
            # base case: <= 2 elements, not sufficient for reordering
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [node for node in arr if node < root]
            right = [node for node in arr if node > root]

            interleaving_ways = comb(len(left) + len(right), len(left))

            return interleaving_ways * solve(left) * solve(right) % MOD

        return (solve(nums) - 1) % MOD