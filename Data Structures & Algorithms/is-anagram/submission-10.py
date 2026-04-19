class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ct = defaultdict(int)
        for c in range(len(s)):
            ct[s[c]] += 1
            ct[t[c]] -=1
        return max(ct.values()) == 0 and min(ct.values()) == 0
