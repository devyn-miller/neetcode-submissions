class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        c_p = defaultdict(list)
        for a,b in prerequisites:
            c_p[a].append(b)
        visiting = set()
        def dfs(c):
            if c not in c_p:
                return True
            if c in visiting:
                return False
            visiting.add(c)
            for ne in c_p[c]:
                if not dfs(ne):
                    return False
            visiting.remove(c)
            # del c_p[c]
            return True
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
