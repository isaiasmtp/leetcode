from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, buy = 0, prices[0]

        for sell in prices:
            if buy < sell:
                if sell - buy > 0:
                    max_profit += sell - buy
                    buy = sell
            else:
                buy = sell
        return max_profit

prices = [7,1,5,3,6,4]
res = Solution().maxProfit(prices)
print(res)