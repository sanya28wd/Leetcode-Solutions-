class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        n=len(matrix)
        m=len(matrix[0])
        i=0
        j=m-1
        while(i<n and j>=0):
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                j-=1
            else:
                i+=1

        return False