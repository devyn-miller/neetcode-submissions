class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = str(s[0])
        if len(s)==1:
            return s
        def longest(l,r):
            res = s[l:r+1]
            while l>=0 and r<len(s) and s[l]==s[r]:
                res = s[l:r+1]
                l -= 1
                r += 1
            return res
        for i in range(len(s)):
            re = longest(i, i)
            if len(re) > len(res):
                res = re
            if i<len(s)-1 and s[i]==s[i+1]:
                re = longest(i, i+1)
                if len(re)>len(res):
                    res = re
        return res