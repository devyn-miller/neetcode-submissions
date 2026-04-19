class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        window = set(s[0])
        m = 1
        l = 0
        for r in range(1,len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            m = max(m,1+ r-l)
            window.add(s[r])
        return m
            
