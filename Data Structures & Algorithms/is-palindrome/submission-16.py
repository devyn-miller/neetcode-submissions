class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        x = ''.join(i.lower() for i in s if i.isalnum())
        if len(x)<=1:
            return True
        print(x)
        r = 0
        l = len(x)-1
        while x[r] == x[l] and r<=l:
            r += 1
            l -= 1
            if r>=l:
                return True
        return False
