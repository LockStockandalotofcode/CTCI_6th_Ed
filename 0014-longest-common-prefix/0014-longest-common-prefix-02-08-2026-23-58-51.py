class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Sort strings lexicographically
        strs.sort()

        # Take first and last strings
        first, last = strs[0], strs[-1]

        result = ""

        # Only compare characters up to the length of the shorter of the two strings
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                result += first[i]
            else:
                return result 
        
        return result