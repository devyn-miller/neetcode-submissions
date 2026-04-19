class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts=[0] * 26
        for l in s:
            counts[ord(l)-ord('a')] += 1
        for l in t:
            counts[ord(l)-ord('a')] -= 1
        for c in counts:
            if c!=0:
                return False
        return True