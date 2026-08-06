class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        ct = [0]*26
        for i in range(len(magazine)):
            ct[ord(magazine[i]) - ord('a')] += 1
            if i < len(ransomNote):
                ct[ord(ransomNote[i]) - ord('a')] -= 1
        return min(ct)>= 0
