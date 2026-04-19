class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[' : ']'}
        for p in s:
            if p in pairs:
                stack.append(p)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if pairs[x] != p:
                    return False
        return True if not stack else False