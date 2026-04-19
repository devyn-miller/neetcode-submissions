class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW=len(matrix)
        COL=len(matrix[0])
        l,r=0,ROW*COL -1
        
        while l<=r:
            m=l+(r-l)//2
                
            row=m//COL
            col=m%COL
            
            if matrix[row][col]>target:
                r=m-1
            elif matrix[row][col]<target:
                l=m+1
            else:return True
            #row=m//col
            #col=m%col
        return False

