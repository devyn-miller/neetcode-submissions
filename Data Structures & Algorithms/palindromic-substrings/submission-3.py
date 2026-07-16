class Solution:
    def countSubstrings(self, s: str) -> int:
        tot = 0
        def count(l, r):
            ct = 0
            while l >= 0 and r< len(s) and s[l] == s[r]:
                ct += 1
                l -=1
                r += 1
            return ct


        for i in range(len(s)):
            tot += count(i, i)
            if i < len(s) - 1:
                tot += count(i, i+1)
        return tot
