class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = defaultdict(set)
        trusters = set(i[0] for i in trust)
        for person, cand in trust:
            adj[cand].add(person)
        for cand in adj:
            if len(adj[cand]) == n - 1:
                if cand not in trusters:
                    return cand
        return -1