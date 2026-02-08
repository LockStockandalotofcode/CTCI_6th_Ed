class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the string of all non0-alphanumeric characters
        clean_s = "".join(char.lower() for char in s if char.isalnum())
        # Check if string is palindrome
        return clean_s == clean_s[::-1]