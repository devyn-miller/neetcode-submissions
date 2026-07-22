class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        c_p = defaultdict(list)
        for c, p in prerequisites:
            c_p[c].append(p)
        visiting = set()
        visited = set()
        res = []
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for nei in c_p[course]:
                if not dfs(nei):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        for i in range(numCourses):
            if i not in visited:
                res.append(i)

        return res
                
            