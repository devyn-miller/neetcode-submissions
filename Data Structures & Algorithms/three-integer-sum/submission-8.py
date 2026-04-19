class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        re=set()
        def twoSum(nums, target):
            seen = set()
            pairs = set()
            for v in nums:
                diff = target - v
                if diff in seen:
                    pairs.add((diff,v))
                seen.add(v)
            if not pairs:
                return False
            return pairs
        for i in range(len(nums)):
            if not twoSum(nums[i+1:],-nums[i]):
                continue
            v = twoSum(nums[i+1:],-nums[i])
            for val in v:
                re.add((nums[i],val[0],val[1]))
        if not re:
            return []
        return [list(v) for v in re]

