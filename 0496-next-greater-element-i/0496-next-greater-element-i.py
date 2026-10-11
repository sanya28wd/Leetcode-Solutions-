class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        s=[]
        new_dict={}
        new_array=[]
        for i in range(len(nums2)-1,-1,-1):
            while(len(s)>0 and s[-1]<=nums2[i]):
                s.pop()
            if not s:
                new_dict[nums2[i]]=-1
            else:
                new_dict[nums2[i]]=s[-1]
            s.append(nums2[i])

        for i in range(0,len(nums1)):
            new_array.append(new_dict[nums1[i]])
        
        return new_array


                
        