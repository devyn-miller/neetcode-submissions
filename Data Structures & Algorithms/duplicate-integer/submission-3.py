class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums)<2:
            return False
        for i,n in enumerate(nums):
            if n == nums[i-1]:
                return True
        return False