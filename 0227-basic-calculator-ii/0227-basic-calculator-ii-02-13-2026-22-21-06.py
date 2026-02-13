class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0
        
        num = 0
        sign = '+'
        stack = []

        # Make a set for easy lookups for operators
        operators = {'+', '-', '*', '/'}

        for i, char in enumerate(s):
            if char.isdigit():
                num = num*10 + int(char)
            
            if char in operators or i == len(s) - 1:
                if char == ' ' and i != len(s) - 1:
                    continue

                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    # // operator rounds -ve answer down to -infinty
                    # int(a/b) rounds down to zero as required
                    prev = stack.pop()
                    stack.append(int(prev / num))
                
                # Update sign for next number and reset num
                sign = char
                num = 0

        return sum(stack)