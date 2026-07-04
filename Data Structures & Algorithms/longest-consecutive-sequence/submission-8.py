class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = set(nums)
        ma = [1]*len(nums)
        m = 1
        for i in range(len(nums)):
            v = 1
            while nums[i]+v in n:
                v += 1
                m = max(m, v)
        return m
            