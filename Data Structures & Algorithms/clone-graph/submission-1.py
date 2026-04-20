"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = defaultdict()
        def dfs(node):
            if node in seen:
                return seen[node]
            x=Node(node.val)
            seen[node] = x
            for n in node.neighbors:
                x.neighbors.append(dfs(n))
            return x
        return dfs(node) if node else None