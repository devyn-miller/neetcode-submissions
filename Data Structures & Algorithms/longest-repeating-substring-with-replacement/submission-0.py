class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        see = Counter()
        m = 0
        l=0
        for r in range(len(s)):
            see[s[r]] += 1
            while (r-l+1) - see[see.most_common(1)[0][0]] > k:
                see[s[l]] -= 1
                l += 1
            m = max(m, r-l+1)
        return m


            