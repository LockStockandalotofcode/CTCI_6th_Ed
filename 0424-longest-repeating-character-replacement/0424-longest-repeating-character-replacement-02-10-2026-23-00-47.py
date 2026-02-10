class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        max_f = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            max_f = max(max_f, count[s[r]])

            # The window is valid if: (length of window - count of most frequent character) <= k. If invalid, shrink from the left.
            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1

            # Update result, at each step the window is valid.
            # Record the maximum length
            res = max(res, r - l + 1)
            
        return res