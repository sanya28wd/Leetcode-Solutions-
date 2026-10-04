class Solution(object):
    def spiralOrder(self, matrix):
        srow=0
        scol=0
        n=len(matrix)
        m=len(matrix[0])
        erow=n-1
        ecol=m-1
        new_array=[]
        elements=0
        while(elements<(n*m)):
            #traverse top
            for j in range(scol,ecol+1):
                new_array.append(matrix[srow][j])
                elements+=1

            #traverse right
            for i in range(srow+1,erow+1):
                new_array.append(matrix[i][ecol])
                elements+=1

            #traverse bottom 
            if srow<erow:
                for j in range(ecol-1,scol-1,-1):  #start,stop,step
                    new_array.append(matrix[erow][j])
                    elements+=1

            #traverse left 
            if scol<ecol:
                for i in range(erow-1,srow,-1):
                    new_array.append(matrix[i][srow])
                    elements+=1

            srow+=1
            scol+=1
            erow-=1
            ecol-=1 

        return new_array

                   