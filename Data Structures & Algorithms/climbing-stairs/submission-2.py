class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if n == 3:
            return 3
        di = [[1,1],[2,2]]
        def re(i):
            if i==n:
                return
            di_n_1, di_val_1 = di[0]

            di_n_2, di_val_2 = di[1]

            di[0] = di[1]
            di[1] = [di_n_2+1, di_val_1 + di_val_2]

            print(di)
            return re(di[1][0])

        re(3)
        return di[1][1]