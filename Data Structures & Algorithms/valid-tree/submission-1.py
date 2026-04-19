class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        visiting = set()
        def dfs(node,prev):
            if node in visiting:
                return False
            visiting.add(node)
            for ne in adj[node]:
                if ne!=prev:
                    if not dfs(ne,node):
                        return False
            return True
        return dfs(0,-1) and len(visiting)==n
            
            
            