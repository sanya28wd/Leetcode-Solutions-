class Solution(object):
    def subarraySum(self, nums, k):
        cur_sum=0
        no_of_subarrays=0
        prefix_sum={0:1}
        for i in nums:
            cur_sum+=i
            diff=cur_sum-k
            no_of_subarrays+=prefix_sum.get(diff,0)
            prefix_sum[cur_sum]=1+prefix_sum.get(cur_sum,0)
        return no_of_subarrays
        
