class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # BASE CASE
        if not digits:
            return []
        
        # HASH MAP OF CONFIGURATIONS
        phone_map = {
            "2" : "abc", "3" : "def","4" : "ghi","5" : "jkl","6" : "mno","7" : "pqrs","8" : "tuv","9" : "wxyz"
        }

        queue = deque([""])

        # for each digit, remove current combinations in res, append its contribution letters to res, then put them back in the res string
        for digit in digits:
            letters = phone_map[str(digit)]
            level_size = len(queue) 

            for _ in range(level_size):
                curr_combination = queue.popleft()
                
                for letter in letters:
                    queue.append(curr_combination + letter)
            
        res = list(queue)
        return res