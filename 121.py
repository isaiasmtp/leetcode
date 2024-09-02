from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, buy = 0, prices[0]
        for sell in prices:
            if buy < sell:
                max_profit = max(sell - buy, max_profit)
            else:
                buy = sell
        return max_profit

prices = [7,1,5,3,6,4]
res = Solution().maxProfit(prices)
print(res)