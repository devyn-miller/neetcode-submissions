class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        if nums[l]==target:
            return l
        if nums[r]==target:
            return r
        def region(l,r):
            while l<r:
                m = l+(r-l)//2
                if nums[l]==target:
                    return l
                if nums[r]==target:
                    return r
                if nums[m]==target:
                    return m
                if nums[m]<target:
                    l = m+1
                else:
                    r = m-1
            return -1
        while l<=r:
            m = l+(r-l)//2
            if nums[l]==target:
                return l
            if nums[r]==target:
                return r
            if nums[m]==target:
                return m
            if nums[r]>nums[m]:
                if nums[m]<target<nums[r]:
                    return region(m+1,r)
                r = m - 1
            else:
                if nums[l]<target<nums[m]:
                    return region(l,m-1)
                l = m + 1
        return -1

