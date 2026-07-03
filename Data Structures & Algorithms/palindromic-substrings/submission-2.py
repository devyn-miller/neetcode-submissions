class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s)==1:
            return 1
        ct = 0
        def sub(l,r):
            nonlocal ct
            while l>=0 and r<len(s) and s[l]==s[r]:
                ct += 1
                l-=1
                r+=1
        for i in range(len(s)):
            if i<len(s)-1 and s[i]==s[i+1]:
                sub(i,i+1)
            sub(i,i)
        return ct