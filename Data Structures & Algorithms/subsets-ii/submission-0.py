class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        nums.sort()
        using = set()
        def backtrack(i):
            if i >= len(nums):
                res.append(tuple(sol[:]))
                return
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
            backtrack(i + 1)
        backtrack(0)
        res = set(res)
        return [list(i) for i in res]