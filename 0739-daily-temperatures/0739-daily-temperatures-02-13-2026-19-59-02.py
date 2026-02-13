class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        stack = [] # Store indices
        res = [0] * n

        for i, t in enumerate(temperatures):
            # while the current temperature is warmer than the index at the top of the stack, pop it and add result to the answer
            while stack and t > temperatures[stack[-1]]:
                stack_idx = stack.pop()
                # difference in indices is the required answer
                res[stack_idx] = i - stack_idx

            # Push current index at top of the stack to compute how fa ahead its warmer is
            stack.append(i)
        
        return res