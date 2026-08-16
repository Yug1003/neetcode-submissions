class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=n-1

        while l<m and r>=0:
            if matrix[l][r]>target:
                r-=1
            elif matrix[l][r]<target:
                l+=1
            else:
                return True
        return False