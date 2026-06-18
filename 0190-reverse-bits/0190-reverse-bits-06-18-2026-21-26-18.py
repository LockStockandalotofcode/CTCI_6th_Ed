class Solution:
    def reverseBits(self, n: int) -> int:
        # bitwise shift method
        result = 0

        for _ in range(32):
            # shift bit to left, make space for new one 
            result <<= 1
            # extract bit from n, then add into result 
            result |= (n & 1)
            # shift n to the right, bring next bit into rightmost position
            n >>= 1

        return result
