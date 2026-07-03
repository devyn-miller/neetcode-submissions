class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        one, two = 1, 2
        for i in range(3,n+1):
            one, two = two, one + two
        return two