class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        # dp = [0]*(len(nums)+1)
        # dp[0],dp[1] = nums[0], max(nums[0],nums[1])
        first, second = nums[0], max(nums[0],nums[1])
        for i in range(2,len(nums)):
            first, second = second, max(first + nums[i], second)

        return max(first, second)