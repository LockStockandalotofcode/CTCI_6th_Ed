class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track_dict = {} # char -> index
        max_length = 0
        left = 0

        for right, char in enumerate(s):
            if char in track_dict and track_dict[char] >= left:
                # remove the preivous duplicate and 
                # jump left pointer to the right of the previous duplicate
                left = track_dict[char] + 1

            track_dict[char] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length