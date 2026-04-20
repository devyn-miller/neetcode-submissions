class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bi(arr):
            if arr[0]==target or arr[-1]==target:
                return True
            l,r = 0,len(arr)-1
            while l<=r:
                m=l+(r-l)//2
                if arr[m]==target:
                    return True
                if arr[m]>target:
                    r = m-1
                if arr[m]<target:
                    l = m+1
            return False
        if matrix[0][0] <= target <= matrix[0][-1]:
            return bi(matrix[0])
        if matrix[-1][0] <= target <= matrix[-1][-1]:
            return bi(matrix[-1])
        l,r = 0, len(matrix)-1
        while l<=r:
            m = l + (r-l)//2
            if matrix[m][0] <= target <= matrix[m][-1]:
                return bi(matrix[m])
            if matrix[m][0] > target:
                r = m-1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                return False
        return False