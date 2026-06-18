class Solution:
    # caching
    _cache = {}

    def _reverseByte(self, byte: int) -> int:
        """Helper for reversing 1 byte or 8 bits at once"""
        # if existing in cache, call from cache
        # return value
        if byte in self._cache:
            return self._cache[byte]

        # else calculate and store in cache
        # return value
        res = 0
        temp = byte

        for _ in range(8):
            res = (res << 1) | (temp & 1)
            temp >>= 1
        
        self._cache[byte] = res
        return res

    def reverseBits(self, n: int) -> int:
        # make set of 4 bytes
        # bitwise AND operation to isolate last 8 bits (least significant byte)
        # reverse bytes individually
        # below are corresponding reversed bytes
        byte0 = self._reverseByte(n & 0xff)
        byte1 = self._reverseByte((n >> 8) & 0xff)
        byte2 = self._reverseByte((n >> 16) & 0xff)
        byte3 = self._reverseByte((n >> 24) & 0xff)

        # join reversed bytes such that entire n is reversed
        res = (byte0 << 24) | (byte1 << 16) | (byte2 << 8) | (byte3)

        return res