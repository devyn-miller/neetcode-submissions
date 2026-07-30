class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_pre = defaultdict(list)
        for course, pre in prerequisites:
            course_pre[course].append(pre)
        visited = set()
        visiting = set()
        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for nei in course_pre[course]:
                if not dfs(nei):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True