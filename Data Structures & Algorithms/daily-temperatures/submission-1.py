class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temperatures = [[t, 0] for t in temperatures]
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]][0] < t[0]:
                curr = stack.pop()
                if temperatures[curr][0] < t[0]:
                    temperatures[curr][1] = i - curr
            stack.append(i)
        return list(v for t,v in temperatures)