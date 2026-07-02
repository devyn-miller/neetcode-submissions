class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        res=0
        def search(l,r):
            res = 0
            while l>-1 and r<len(s) and s[l] == s[r]:
                    res +=1
                    l-=1
                    r+=1
            return res

        for i in range(len(s)):
            res += search(i,i)
            res += search(i,i+1)
        return res
