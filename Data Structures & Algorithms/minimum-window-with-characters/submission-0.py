class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ''
        count = Counter(t)
        char_remain = len(count)
        l=0
        idx = []
        mi = float('inf')
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]]-=1
                if count[s[r]] == 0:
                    char_remain -=1
            while l<=r and char_remain == 0:
                if r-l+1 < mi:
                    mi = r-l+1
                    idx = [l,r]
                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] > 0:
                        char_remain +=1
                l+=1
                        
        if idx:
            return s[idx[0]:idx[1]+1]
        return ''
