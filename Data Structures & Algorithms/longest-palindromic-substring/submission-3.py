class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=''
        if len(s)==1 or s == '':
            return s
        def search(l,r):
            res = s[l:r+1]
            for i in range(len(s)):
                if l<0 or r>len(s)-1:
                    break
                if s[l] == s[r]:
                    res = s[l:r+1]
                    if l-1>-1:
                        l-=1
                    if r+1<len(s):
                        r+=1
                else:
                    break
            return res

        for i in range(len(s)-1):
            temp = search(i,i)
            if len(res)< len(temp):
                res = temp
            if s[i]==s[i+1]:
                temp = search(i,i+1)
                if len(res)< len(temp):
                    res = temp
        return res