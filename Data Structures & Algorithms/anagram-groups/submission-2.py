class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for st in strs:
            cts = [0]*26
            for s in st:
                cts[ord(s)-ord('a')] += 1
            dic[tuple(cts)].append(st)
        return list(dic.values())
            