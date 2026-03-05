class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I' : 1,
               'V' : 5,
               'X' : 10,
               'L' : 50,
               'C' : 100,
               'D' : 500,
               'M' : 1000}
        
        n = len(s)
        res = 0
        for i in range(n): # iterates from 0 upto n, excluding the number n
            # If we're not at the last character, and current is smaller than next character
            if i < n-1 and map[s[i]] < map[s[i+1]]:
                # subtract from the number
                res -= map[s[i]]
            else:
                # add to the number
                res += map[s[i]]
        
        return res