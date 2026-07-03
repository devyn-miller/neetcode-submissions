class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in range(len(strs)):
            bucket = [0]*26
            t = strs[i]
            strs[i] = list(strs[i])
            for s in strs[i]:
                bucket[ord(s) - ord('a')] += 1
            dic[tuple(bucket)].append(t)
        return list(dic.values())
        

        