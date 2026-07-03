class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        def helper(num):
            if len(num) < 3:
                return max(num)
            one, two = num[0], max(num[0:2])
            for i in range(2, len(num)):
                one, two = two, max(one+num[i], two)
            return max(one,two)
        return max(helper(nums[1:]), helper(nums[:-1]))