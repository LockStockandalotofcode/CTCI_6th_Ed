class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): # any number with trailing zeroes is not a palindrome, since it must start with 0 as well
            return False
        
        revertedNum = 0
        while x > revertedNum:
            revertedNum = (revertedNum * 10) + (x % 10)
            x //= 10

        return x == revertedNum or x == revertedNum // 10
        # the division by 10, takes care of odd length numbers, it gets rid of the middle number