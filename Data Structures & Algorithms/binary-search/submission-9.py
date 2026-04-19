class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x=nums
        if len(nums)==1:
            if nums[0]==target: return 0
        guess=len(nums)//2
        while len(x) > 1:
            print(guess)
            if nums[guess] < target:
                if nums[guess+1]> target:
                    return -1
                if nums[guess+1]==target:
                    return guess+1
                x = x[guess:]
                guess+=len(x)//2
            elif nums[guess] > target:
                if nums[guess-1] < target:
                    return -1
                if nums[guess-1]==target:
                    return guess-1
                x = x[:guess]
                guess-=len(x)//2
            else:
                return guess
            if guess==1:
                if nums[guess]==target:
                    return guess
        return -1
        