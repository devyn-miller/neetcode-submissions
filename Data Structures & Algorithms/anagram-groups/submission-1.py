class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        re = defaultdict(list)
        for w in strs:
            count = [0]*26
            for l in w:
                count[ord(l)-ord('a')] += 1
            re[tuple(count)].append(w)
        return list(re.values())