class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for course, pre in prerequisites:
            courses[course].append(pre)
        visited = set()
        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for nei in courses[course]:
                if not dfs(nei):
                    return False
            visited.add(course)
            return True
        for i in range(numCourses):
            visiting = set()
            if not dfs(i):
                return False
        return True

