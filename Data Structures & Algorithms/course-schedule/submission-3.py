class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cour_pre = defaultdict(list)
        for cour, pre in prerequisites:
            cour_pre[cour].append(pre)
        visiting = set()
        visited = set()
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for nei in cour_pre[course]:
                if not dfs(nei):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
