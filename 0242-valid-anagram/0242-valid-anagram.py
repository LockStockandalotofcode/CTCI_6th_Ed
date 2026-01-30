class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Length check
        if len(s) != len(t):
            return False
        # Dictionary to keep track of characters encountered
        # key = character, value = frequency of character
        track = {}

        for char in s:
            # If char isnt there in track dict, start at 0 and add 1
            track[char] = track.get(char, 0) + 1

        for char in t:
            if char not in track or track[char] == 0:
                return False
            else:
                track[char] -= 1

        return True
