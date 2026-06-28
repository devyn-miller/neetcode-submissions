class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        cache = [1]*len(nums)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    cache[j] = max(cache[i]+1, cache[j])


            
        return max(cache)
            
                
                    

