class Solution(object):
    def majorityElement(self, nums):
        
        n=len(nums)
        majority=nums[0]
        votes=1
        for i in range(1,n):
            if votes==0:
                majority=nums[i]
                votes+=1
            elif nums[i]==majority:
                votes+=1
            else:
                votes-=1
        return majority
            
