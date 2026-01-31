class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        doubled_string = goal + goal
        if s in doubled_string:
            return True
        return False 