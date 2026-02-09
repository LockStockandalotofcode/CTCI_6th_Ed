class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s:
            return 0
        
        sign = 1
        i = 0

        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result*10 + int(s[i])
            i += 1

        result *= sign 

        MAX_INT = 2**31 - 1
        MIN_INT = - 2**31

        if result > MAX_INT:
            return MAX_INT
        elif result < MIN_INT:
            return MIN_INT
        
        return result