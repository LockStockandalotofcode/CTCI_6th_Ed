from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Counter creates a frequency map automatically
        # e.g., Counter("aabbc") -> {'a': 2, 'b': 2, 'c': 1}

        counts = Counter(magazine)
        
        for ch in ransomNote:
            if counts[ch] <= 0:
                return False
            counts[ch] -= 1
            
        return True