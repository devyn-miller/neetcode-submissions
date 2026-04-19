class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {'}':'{',']':'[',')':'('}
        for i in range(len(s)):
            if s[i] in pairs:
                if len(stack)<1:
                    return False
                if stack.pop()!=pairs[s[i]]:
                    return False
            else:
                stack.append(s[i])
        if len(stack)>0:
            return False
        return True
                    
