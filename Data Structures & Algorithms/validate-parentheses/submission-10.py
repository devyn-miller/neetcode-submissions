class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '{': '}', '[' : ']'}
        stack = []
        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            else:
                if not stack or (stack and stack.pop() != char):
                    return False
        return len(stack) == 0