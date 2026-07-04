class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l, r = 0, 1
        m = 1
        cur = set(s[0])
        while r<len(s):
            while s[r] in cur:
                cur.remove(s[l])
                l+=1
            cur.add(s[r])
            m = max(m,len(cur))
            r += 1
        return m
