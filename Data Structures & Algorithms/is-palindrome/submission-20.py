class Solution:
    def isPalindrome(self, s: str) -> bool:
        i =len(s)-1
        for idx,c in enumerate(s):
            if not c.isalnum():
                continue
            while not s[i].isalnum():
                i-=1
    
            if s[i].lower()!= c.lower():
                return False
                
            i-=1
        return True
        