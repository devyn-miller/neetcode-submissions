class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[i.lower() for i in s if i.isalnum()]
        if s==s[::-1]:
            return True
        return False