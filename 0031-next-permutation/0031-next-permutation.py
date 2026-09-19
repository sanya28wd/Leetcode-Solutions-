class Solution(object):
    def nextPermutation(self, nums):
        "to find the pivot element"
        piv=-1
        n=len(nums)-2
        while(n>=0):
            if nums[n]<nums[n+1]:
                piv=n
                break
            n-=1
        #if its the max permutation we should return the lowest permutation as per the question 
        if piv==-1:
            nums.sort()
            return 

        "to swap the pivot with the element greater than it preferably the last one"

        i=len(nums)-1
        while(i>piv):
            if nums[i]>nums[piv]:
                nums[i], nums[piv] = nums[piv], nums[i]
                break 
            i-=1
        
        "to sort the array basically back to front from the element > pivot"
        nums[piv+1:]=sorted(nums[piv+1:])

        

        



        