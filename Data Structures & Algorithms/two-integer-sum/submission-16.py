class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            if v in seen:
                return sorted([i,seen[v]])
            diff = target - v
            seen[diff] = i
