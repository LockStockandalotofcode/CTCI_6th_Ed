class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # BASE CASE
        if not digits:
            return []
        
        # HASH MAP OF CONFIGURATIONS
        phone_map = {
            "2" : "abc", "3" : "def","4" : "ghi","5" : "jkl","6" : "mno","7" : "pqrs","8" : "tuv","9" : "wxyz"
        }

        res = []
        temp = [] 
        # one full string at a time is to be formed in temp
        # used to store characters of a full string 
        # once completed, made into string and saved to results list

        def backtrack(pos: int):
            # tracks the pos in digits reached, to check completion of string 
            # once completed, made into string and saved to results list
            if pos == len(digits):
                res.append("".join(temp))
                return

            # get map corresponding to letter
            curr_digit = digits[pos]
            letters = phone_map[curr_digit]

            # go over each letter, take it to completion of full length string
            for letter in letters:
                temp.append(letter) 
                backtrack(pos + 1)
                temp.pop()
        
        backtrack(0)
        return res