class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,post=1,1
        re=[1]*len(nums)
        for i in range(len(nums)):
            re[i]=pre
            pre*=nums[i]
        print(re)
        for i in range(len(nums)-1,-1,-1):
            re[i]*=post
            post*=nums[i]
        print(re)
        return re
            


