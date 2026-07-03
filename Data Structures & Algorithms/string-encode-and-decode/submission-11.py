class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word))
            res += '#'
            res += word
        return res


            


    def decode(self, s: str) -> List[str]:
        res = []
        le = 0
        i = 0
        while i < len(s):
            nu = i
            while s[nu]!='#':
                nu += 1
            le = int(s[i:nu])
            res.append(s[nu + 1:nu + 1 + le])
            i = nu + 1 + le
        return res
        

