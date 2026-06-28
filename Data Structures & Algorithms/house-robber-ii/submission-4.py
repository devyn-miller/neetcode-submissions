class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        def helper(num):
            n = len(num)
            if n<3:
                return max(num)
            num[2] += num[0]
            for i in range(3,n):
                num[i] += max(num[:i-1])
            return max(num)
        return max(helper(nums[1:]),helper(nums[:-1]))

        


        



