class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))
        rank = [0]*n
        def find(node):
            while par[node]!=node:
                par[node] = par[par[node]]
                node = par[node]
            return node
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 0
            if par[p1]>par[p2]:
                par[p2] = p1
                rank[p1]+=rank[p2]
            else:
                par[p1] = p2
                rank[p2]+=rank[p1]
            return 1
        re = n
        for n1,n2 in edges:
            re-= union(n1,n2)
        return re
