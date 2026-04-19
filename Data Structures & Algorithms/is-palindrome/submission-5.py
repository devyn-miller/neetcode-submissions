class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for i in s:
            if i.isalpha():
                l.append(i.lower())
            elif i.isnumeric():
                l.append(i)
        if l == l[::-1]:
            return True
        return False