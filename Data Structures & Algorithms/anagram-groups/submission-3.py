class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            temp = [0]*26
            for ch in word:
                temp[ord(ch) - ord('a')] += 1
            t = tuple(temp)
            groups[t].append(word)
        return list(groups.values())