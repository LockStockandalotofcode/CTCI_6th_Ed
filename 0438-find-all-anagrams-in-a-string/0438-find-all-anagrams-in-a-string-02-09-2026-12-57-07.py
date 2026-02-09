class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []
        
        p_count = Counter(p)
        s_count = Counter()

        result = []
        
        for i in range(ns):
            # Add current character
            s_count[s[i]] += 1

            # Remove the character that left the window
            if i >= np:
                left_char = s[i - np]
                if s_count[left_char] == 1:
                    del s_count[left_char]
                else:
                    s_count[left_char] -= 1

            # Compare maps
            if p_count == s_count:
                result.append(i - np + 1)

        return result