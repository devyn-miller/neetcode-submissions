class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        nums=set(nums)
        m=1
        curr = 1
        
        for n in nums:
            while n + curr in nums:
                curr +=1
            m = max(m,curr)
            curr = 1

        return m