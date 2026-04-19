class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        print(nums)
        cur = 1
        longest = 1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                cur += 1
                print(cur)
                if cur == len(nums):
                    return len(nums)
                if cur > longest:
                    longest = cur
            else:
                cur = 1


        return longest