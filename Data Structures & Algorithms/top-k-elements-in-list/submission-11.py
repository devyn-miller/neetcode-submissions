class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter()
        counter.update(nums)
        return [c[0] for c in counter.most_common(k)
]