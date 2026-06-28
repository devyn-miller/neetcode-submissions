class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2)>len(text1):
            text1,text2=text2,text1
        horizontal = len(text2)
        vertical = len(text1)
        dp = [0]*(vertical+1)
        
        for i in range(vertical-1, -1, -1):
            curr = 0
            for j in range(horizontal-1, -1, -1):
                temp = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = curr + 1
                    
                else:
                    dp[j] = max(dp[j], dp[j+1])
                curr = temp


        return dp[0]


                

