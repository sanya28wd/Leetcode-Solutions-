class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        sell=0
        max_profit=0
        for i in prices:
            if i < buy:
                buy=i
            elif i-buy>max_profit :
                max_profit=i-buy
                sell=i
                
        return max_profit

