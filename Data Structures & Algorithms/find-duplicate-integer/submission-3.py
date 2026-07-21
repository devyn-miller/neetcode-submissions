class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i, v in enumerate(nums):
            if nums[abs(v)-1] < 0:
                return abs(v)
            nums[abs(v)-1] *= -1