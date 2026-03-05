from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Counter creates a frequency map automatically
        # e.g., Counter("aabbc") -> {'a': 2, 'b': 2, 'c': 1}
        # Counter supports subtraction, if below is not empty, it means magazine had everything that was needed

        return not (Counter(ransomNote) - Counter(magazine))