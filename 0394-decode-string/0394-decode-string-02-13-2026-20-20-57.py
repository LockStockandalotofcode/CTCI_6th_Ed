class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
                # for numbers with more than one digit 
                curr_num = curr_num * 10 +  int(char)
            elif char == '[':
                # push string built so far and the multiplier
                stack.append((curr_str, curr_num))
                # reset for new nested context
                curr_str = ""
                curr_num = 0
            elif char == ']':
                # Pop the outer string and the multiplier
                prev_str, num = stack.pop()
                # repeat the current string and attach to outer string
                curr_str = prev_str + (curr_str * num)
            else:
                # regular characters
                curr_str += char            

        return curr_str