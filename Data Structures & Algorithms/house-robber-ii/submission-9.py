class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<4:
            return max(nums)
        def helper(nums):

            nums[2] = max(nums[2]+nums[0],nums[1])
            for i in range(3, len(nums)):
                nums[i] += max(nums[i-2], nums[i-3])
            return max(nums)
        return max(helper(nums[1:]),helper(nums[:-1]))