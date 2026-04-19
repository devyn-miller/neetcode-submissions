class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<=r:
            while l<=r and not s[l].isalnum():
                l+=1
            while l<=r and not s[r].isalnum():
                r-=1
            if l<=r:
                sr,sl=s[r],s[l]
                if s[l].isalpha:
                    sl = s[l].lower()
                if s[r].isalpha:
                    sr=s[r].lower()
                if sr!=sl:
                    return False
            l+=1
            r-=1
        return True