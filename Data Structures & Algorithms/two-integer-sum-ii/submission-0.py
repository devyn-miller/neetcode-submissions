class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = len(numbers)-1
        right = 0
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                left -= 1
            else:
                right += 1
        return [right+1,left+1]