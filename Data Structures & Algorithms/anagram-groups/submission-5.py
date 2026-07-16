class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            bucket = [0]*26
            for c in word:
                bucket[ord(c) - ord('a')] += 1
            groups[str(bucket)].append(word)
        return list(groups.values())