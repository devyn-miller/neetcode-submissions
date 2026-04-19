class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l,r = 0,len(nums)-1
        if nums[l]<nums[r]:
            return nums[l]
        while l<r:
            mid = l + (r-l)//2
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r=mid

        return min(nums[l],nums[r])




