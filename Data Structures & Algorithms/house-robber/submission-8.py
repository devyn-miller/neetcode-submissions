class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        nums[2] = max(nums[2]+nums[0],nums[1])
        for i in range(3, len(nums)):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums)