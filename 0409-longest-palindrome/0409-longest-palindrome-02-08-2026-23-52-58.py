class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        count_dict = {}

        for char in s:
            count_dict[char] = count_dict.get(char, 0) + 1
        
        length = 0
        has_odd = False

        for _, count in count_dict.items():
            if count%2 == 0:
                length += count
            else:
                # Use the even part (e.g., if count is 5, use 4)
                length += (count - 1)
                has_odd = True
            
        # if atleast one odd, we can put at most 1 char in the middle
        if has_odd:
            length += 1
        
        return length