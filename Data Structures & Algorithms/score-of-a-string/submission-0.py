class Solution:
    def scoreOfString(self, s: str) -> int:
        tot=0
        seen=[None] * len(s)
        for i,v in enumerate(s):
            ascii = ord('a') + ord(v)
            seen[i]=ascii
        print(seen)
        # seen.append(s[-1])
        print(len(s),len(seen))
        for i,v in enumerate(seen[:-1]):
            # if i <= len(s):
            tot += abs(seen[i]-seen[i+1])

        return tot


        