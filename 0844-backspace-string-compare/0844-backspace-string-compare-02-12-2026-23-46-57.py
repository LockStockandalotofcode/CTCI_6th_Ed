class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []
        for char in s:
            if char.isalnum():
                stack1.append(char)
            elif stack1:
                stack1.pop()
            
        for char in t:
            if char.isalnum():
                stack2.append(char)
            elif stack2:
                stack2.pop()
        
        return stack1 == stack2