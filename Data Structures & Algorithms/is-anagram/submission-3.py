class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t = list(i for i in t)
        for l in s:
            if l in t:
                t.remove(l)
            else:
                return False
        return True