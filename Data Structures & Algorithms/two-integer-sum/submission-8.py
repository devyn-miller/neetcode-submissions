class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==2:
            return [0,1]
        n2=sorted(nums)
        l = 0
        r = len(n2) - 1
        for n in n2:
            if n2[l]+n2[r]==target:
                print(r,l)
                if nums.index(n2[l])==nums.index(n2[r]):
                    x=nums.index(n2[r])
                    re=x
                    nums[x]='_'
                    return sorted([re, nums.index(n2[r])])
                return sorted([nums.index(n2[l]), nums.index(n2[r])])
            elif n2[l]+n2[r]>target:
                r+=-1
            else:
                l+=1
        