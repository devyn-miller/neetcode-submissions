class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = [1]*(len(nums)+1)
        pre = 1
        suff = 1
        for i in range(1,len(nums)):
            pre *= nums[i-1]
            out[i] = pre
        for i in range(len(nums)-1,-1,-1):
            print(i)
            out[i]*=suff
            suff *= nums[i]
            print(nums,out)
        return out[:-1]
            
            
