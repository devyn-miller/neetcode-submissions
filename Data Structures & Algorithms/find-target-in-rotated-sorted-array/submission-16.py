class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            if nums[0]<nums[-1]:
                break
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid]<nums[right]:
                right = mid
            else:
                left = mid + 1
        pivot = left
        if nums[pivot]==target:
            return pivot
        if nums[right]==target:
            return right
        if nums[pivot]<target<=nums[-1]:
            l,r=pivot+1,len(nums)-1
        else: l,r=0,pivot-1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid + 1
        return -1




