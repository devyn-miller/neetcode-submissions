class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [(0, temperatures[0])]
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                idx, temp = stack.pop()
                res[idx] = i - idx
            stack.append((i, v))
        return res