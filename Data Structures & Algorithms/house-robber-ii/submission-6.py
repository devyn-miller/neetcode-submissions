class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        def helper(num):
            if len(num)<3:
                return max(num)
            first,second = num[0],max(num[0], num[1])
            for i in range(2,len(num)):
                first,second = second,max(num[i] + first, second)
            return max(first,second)
        return max(helper(nums[1:]),helper(nums[:len(nums)-1]))