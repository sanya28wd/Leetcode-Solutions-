class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length=0
        left=0
        right=0
        new_set=set()
        while(right!=len(s)):
            if s[right] not in new_set:
                new_set.add(s[right])
                right+=1
                max_length=max(max_length,right-left)          
            else:
                new_set.remove(s[left])
                left+=1
                

        return max_length




        