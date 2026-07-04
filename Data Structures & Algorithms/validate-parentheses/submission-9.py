class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']':'[', ')':'(', '}':'{'}
        stck = []
        for v in s:
            if v in pairs:
                if not stck:
                    return False
                if stck.pop() != pairs[v]:
                    return False
            else:
                stck.append(v)
        return False if stck else True