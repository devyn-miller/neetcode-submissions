class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0]==target:
            return 0
        if nums[-1]==target:
            return len(nums)-1
        l,r=0,len(nums)-1
        while l<r:
            m=l+(r-l)//2
            if nums[m]>target:
                r=m
            elif nums[m]<target:
                l=m+1
            else: return m
        return -1

        