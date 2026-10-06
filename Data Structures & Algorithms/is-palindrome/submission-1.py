class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [c.lower() for c in s if c.isalnum()]
        return letters == letters[::-1]