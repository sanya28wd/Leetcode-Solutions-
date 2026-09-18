class Solution(object):

    def searchRow(self,matrix,target,row):
        j=len(matrix[0])
        st=0
        end=j-1
        while(st<=end):
            mid=st+(end-st)//2
            if target==matrix[row][mid]:
                return True
            elif target<matrix[row][mid]:
                end=mid-1
            else:
                st=mid+1
        return False
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False 
        i=len(matrix)
        j=len(matrix[0])
        startrow=0
        endrow=i-1
        while startrow<=endrow:
            midrow=startrow+(endrow-startrow)//2
            if target>=matrix[midrow][0] and target<=matrix[midrow][j-1]:
                "found the row==>find in this row"
                return self.searchRow(matrix,target,midrow)
            elif target>matrix[midrow][j-1]:
                "then go to next row"
                startrow=midrow+1
            else:
                endrow=midrow-1
        return False
        
        
