class Solution(object):
    def maxProfit(self, prices):
        lowest = prices[0]
        max_profit = 0
        for price in prices:
            lowest = min(lowest,price)
            profit = price - lowest
            max_profit = max(max_profit,profit)
        return max_profit
            
        
       
                

        
        