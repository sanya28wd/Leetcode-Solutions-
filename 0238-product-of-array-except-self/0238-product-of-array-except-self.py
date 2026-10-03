class Solution(object):
    def productExceptSelf(self, nums):
        """prod_array=[]
        for i,val_i in enumerate(nums):
            prod=1
            for j,val_j in enumerate(nums):
                if(i!=j):
                    prod=prod*val_j
            prod_array.append(prod)
        return prod_array"""

        res=[1]*(len(nums))
        prefix=1
        for i in range(0,len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res