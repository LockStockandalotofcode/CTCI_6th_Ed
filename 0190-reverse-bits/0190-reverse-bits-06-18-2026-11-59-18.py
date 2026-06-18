class Solution:
    def reverseBits(self, n: int) -> int:
        # decimal to binary string 
        binary_str = bin(n)[2:]
        # pad with leading zeroes
        binary_str = binary_str.zfill(32)
        # reverse bits with slicing 
        reversed_str = binary_str[::-1]
        # convert back to int
        return int(reversed_str, base=2)