class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        a=None
        s=set() 
        no_of_elements=len(grid)
        N=no_of_elements*no_of_elements
        grid_sum=0
        for i in grid:
            for j in i:
                grid_sum+=j
                if j in s:
                    a=j
                s.add(j)

        
     
        actual_sum=(N*(N+1))/2
        b=actual_sum+a-grid_sum
        return [a,b]

