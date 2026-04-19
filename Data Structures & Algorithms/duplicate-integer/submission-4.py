class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <=1:
            return False
        seen = []
        for n in nums:
            if n in seen:
                return True
            seen.append(n)
        return False
         