"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        pairs = {}
        def dfs(nod):
            if nod in pairs:
                return pairs[nod]
            cp = Node(nod.val)
            pairs[nod] = cp
            for nei in nod.neighbors:
                cp.neighbors.append(dfs(nei))
            return cp
        return dfs(node) if node else None

