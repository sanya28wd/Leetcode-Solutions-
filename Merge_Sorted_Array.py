class Solution(object):
    def merge(self, nums1, m, nums2, n):       
        i=m-1
        j=n-1
        p=n+m-1
        while i>=0 and j>=0:
            if nums1[i]>=nums2[j] :
                nums1[p]=nums1[i]
                p-=1
                i-=1
            else:
                nums1[p]=nums2[j]
                p-=1
                j-=1

        while j>=0:
            nums1[p]=nums2[j]
            p-=1
            j-=1
        

