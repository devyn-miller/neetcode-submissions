class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ct = [0]*26
        for i in range(len(s)):
            ct[abs(ord('a') - ord(s[i]))] += 1
            ct[abs(ord('a') - ord(t[i]))] -= 1
        return min(ct) == 0 and max(ct) == 0