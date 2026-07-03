class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s=list(s)
        t=list(t)
        c1 = Counter(s)
        c2 = Counter(t)
        if len(c1)!= len(c2):
            return False
        for v in c1.keys():
            if v not in c2 or c2[v]!= c1[v]:
                return False
        return True