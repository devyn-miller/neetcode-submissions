class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        print(counts)
        # for bucket in range(len(buckets)-1, 0, -1):
        for key, value in counts.items():
            buckets[value].append(key)
        print(buckets)
        res=[]
        for bucket in buckets[::-1]:
            for b in bucket:
                res.append(b)
                k-=1
                if k == 0:
                    return res
        print(res)
            

