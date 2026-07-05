class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for start, end, cost in edges:
            adj[start].append((end, cost))
        shortest = {}
        minHeap = [(0, src)]
        while minHeap:
            cost, dest = heapq.heappop(minHeap)
            if dest in shortest:
                continue
            shortest[dest] = cost
            for e, c in adj[dest]:
                if e not in shortest:
                    heapq.heappush(minHeap, (c + cost, e))
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest
            