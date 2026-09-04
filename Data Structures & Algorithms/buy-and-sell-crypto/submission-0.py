class Solution:
    def __init__(self):
        self.max_profit = 0

    def maxProfit(self, prices: List[int]) -> int:
        for current_day, current_price in enumerate(prices): 
            for future_day, future_price in enumerate(prices[current_day + 1:]): 
                if future_price > current_price: 
                    profit = future_price - current_price
                    if profit > self.max_profit:
                        self.max_profit = profit
        return self.max_profit
        
