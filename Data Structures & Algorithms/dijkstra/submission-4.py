class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for start, dest, weight in edges:
            adj[start].append((weight, dest))
        shortest = {}
        minHeap = [(0, src)]
        while minHeap:
            weight, dest = heapq.heappop(minHeap)
            if dest in shortest:
                continue
            shortest[dest] = weight
            for nei in adj[dest]:
                heapq.heappush(minHeap, (nei[0] + weight, nei[1]))
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest
            