class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n2=nums[1:]
        for idx1,v1 in enumerate(nums):
            for idx2,v2 in enumerate(n2):
                if v1+v2==target:
                    if idx1!=idx2+1:
                        return [idx1,idx2+1]

        