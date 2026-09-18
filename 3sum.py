class Solution(object):
    def threeSum(self, nums):
        """
        1)approach 1
        s=set()
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if(nums[i]+nums[j]+nums[k]==0):
                        s.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        return [list(triplet) for triplet in s]
        """
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                total=nums[i]+nums[j]+nums[k]
                if total<0:
                    j+=1
                elif total>0:
                    k-=1
                elif total==0:
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    
        return result
