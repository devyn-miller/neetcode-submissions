class Solution:
    def countSubstrings(self, s: str) -> int:
        le = len(s)
        if le == 1:
            return 1
        tot = 0
        for i in range(le):
            l,r = i,i
            while l>=0 and r<le and s[l]==s[r]:
                tot+=1
                l-=1
                r+=1
            l,r = i,i+1
            while l>=0 and r<le and s[l]==s[r]:
                tot+=1
                l-=1
                r+=1
        return tot