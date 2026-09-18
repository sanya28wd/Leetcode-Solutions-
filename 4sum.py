class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        final_array=[]
        for i in range(0,len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                m=len(nums)-1
                while(k<m):
                    target_sum=nums[i]+nums[j]+nums[k]+nums[m]
                    if target_sum==target:
                        final_array.append([nums[i],nums[j],nums[k],nums[m]])
                        k+=1
                        m-=1
                        while  k<m and nums[k]==nums[k-1]:
                            k+=1
                        while m>k and nums[m]==nums[m+1]:
                            m-=1
                    elif target_sum<target:
                        k+=1

                    else:
                        m-=1
                    
        return final_array 


        
