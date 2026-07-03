class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        def helper(nums):
            if len(nums) < 3:
                return max(nums)
            nums[1] = max(nums[0:2])
            for i in range(2, len(nums)):
                nums[i]= max(nums[i-2]+nums[i], nums[i-1])
            return max(nums)
        return max(helper(nums[1:]), helper(nums[:-1]))