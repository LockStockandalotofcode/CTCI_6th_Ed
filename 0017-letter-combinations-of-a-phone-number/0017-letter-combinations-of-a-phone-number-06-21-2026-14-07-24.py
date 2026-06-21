import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # BASE CASE
        if not digits:
            return []
        
        # HASH MAP OF CONFIGURATIONS
        phone_map = {
            "2" : "abc", "3" : "def","4" : "ghi","5" : "jkl","6" : "mno","7" : "pqrs","8" : "tuv","9" : "wxyz"
        }

        # PYTHONIC WAY

        # get letter groups corresponding to each digit
        letter_grps = [phone_map[d] for d in digits]

        # generate combinations with cartesian product logic by itertools.product
        # the combinations generated are array of character strings 
        combinations = itertools.product(*letter_grps)
        
        # the combinations generated are array of character strings 
        # make proper strings and make the final list
        return ["".join(c) for c in combinations]