class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_cour = defaultdict(list)
        for pre, cour in prerequisites:
            pre_cour[pre].append(cour)
        state = [0]*numCourses
        out = []
        def dfs(c):
            if state[c] == 1:
                return False
            if state[c] == 2:
                return True
            state[c] = 1
            for ne in pre_cour[c]:
                if not dfs(ne):
                    return False
            state[c] = 2
            out.append(c)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return out
            