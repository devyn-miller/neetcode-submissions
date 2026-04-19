class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        pre_cour = defaultdict(list)
        for pre,cour in edges:
            pre_cour[pre].append(cour)
        state = [0]*n
        self.PATH = []
        def dfs(cour):
            if state[cour] == 1:
                return False
            if state[cour] == -1:
                return True
            state[cour]=1
            for ne in pre_cour[cour]:
                if not dfs(ne):
                    return False
            state[cour] = -1
            self.PATH.append(cour)
            return True
        for cour in range(n):
            if not dfs(cour):
                return []
            else:
                dfs(cour)
        self.PATH.reverse()
        return self.PATH
