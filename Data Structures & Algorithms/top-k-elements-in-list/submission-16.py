class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        dic = defaultdict(list)
        for key,v in Counter(nums).items():
            dic[v].append(key)
        res = []
        i = 0
        while i < k:
            print(dic)
            m = max(dic)
            res.extend(dic[m])
            i += len(dic[m])
            del dic[m]
        return res