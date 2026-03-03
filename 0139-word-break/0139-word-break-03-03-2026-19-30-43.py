class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # convert list to set for O(1) lookups
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)

        # Base case: an empty string is always valid
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                # if the prefix s[0:j] is VALID and the remaining portion is a word in the given word dictiionary, this is valid, move on to the next index 
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]
