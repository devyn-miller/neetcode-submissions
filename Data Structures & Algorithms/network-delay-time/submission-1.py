class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, target, time in times:
            adj[src].append((time, target))
        shortest = {}
        minHeap = [(0, k)]
        seen = set()
        while minHeap:
            cur_time, cur_target = heapq.heappop(minHeap)
            if cur_target in seen:
                continue
            seen.add(cur_target)
            shortest[cur_target] = cur_time
            for time, target in adj[cur_target]:
                if target not in seen:
                    heapq.heappush(minHeap, (cur_time + time, target))
        return max(shortest.values()) if len(shortest) == n else -1
                
        