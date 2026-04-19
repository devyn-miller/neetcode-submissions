class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ''
        for st in strs:
            s += str(len(st))
            s+= '&'
            s += st
        return s


    def decode(self, s: str) -> List[str]:
        out = []
        l,r=0,1
        while r<len(s):
            while s[r] != '&':
                r+=1
            le = int(s[l:r])
            out.append(s[r+1:r+1+le])
            l = r + le + 1
            r = l+1
        return out