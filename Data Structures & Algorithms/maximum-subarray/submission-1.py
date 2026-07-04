class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if max(nums)<=0:
            return max(nums)
        m = max(nums)
        curr = 0
        for n in nums:
            if n < 0 and curr + n < 0:
                curr = 0
            else:
                curr += n
                m = max(m, curr)
        return m
        

