class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in track:
                return [track[diff], i]
            track[v] = i
            
                    
            



        