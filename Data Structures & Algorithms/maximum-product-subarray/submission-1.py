class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        if min(nums) >= 1:
            return math.prod(nums)
        if len(nums)==1:
            return nums[0]
        curr_min, curr_max = 1, 1
        for n in nums:
            curr_min, curr_max = min(curr_min*n, n, curr_max*n), max(curr_min*n, n, curr_max*n)
            res = max(res, curr_min,curr_max)
        return res