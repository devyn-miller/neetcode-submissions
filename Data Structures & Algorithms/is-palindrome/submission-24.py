class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.replace(' ',''))
        for c in s:
            if not c.isalnum():
                s.remove(c)
        s = [c.lower() for c in s]
        s = ''.join(s)
        print(s)
        return s == s[::-1]
