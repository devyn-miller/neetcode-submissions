class Solution:
    def numDecodings(self, s: str) -> int:
        dp1, dp2 = 1, 1
        for i in range(len(s) - 1, -1, -1):
            dp = 1
            if s[i] == '0':
                dp = 0
            elif i<len(s) - 1 and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                dp = dp1 + dp2
            else:
                dp = dp1
            dp1, dp2 = dp, dp1

        return dp
            
