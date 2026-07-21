class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s[0]
        m = 1
        curr = ''
        res1, res2 = '', ''
        def length(b, e):
            while b > -1 and e < len(s) and s[b] == s[e]:
                b -= 1
                e += 1
            return str(s[b+1:e])
        for i in range(len(s)):
            res1 = length(i, i)
            if i < len(s) - 1:
                res2 = length(i, i+1)
            if len(res1) > m:
                curr = res1
                m = len(res1)
            if len(res2) > m:
                m = len(res2)
                curr = res2
        if m == 1:
            return s[0]
        return curr
