class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        l1, l2 = len(text1), len(text2)
        prev = [0]*(l2+1)
        curr = [0]*(l2+1)
        for c1 in range(l1-1, -1, -1):
            for c2 in range(l2 - 1, -1, -1):
                if text1[c1] == text2[c2]:
                    curr[c2] = prev[c2 + 1] + 1
                else:
                    curr[c2] = max(curr[c2 + 1], prev[c2])
            prev, curr = curr, prev
        return prev[0]
                    