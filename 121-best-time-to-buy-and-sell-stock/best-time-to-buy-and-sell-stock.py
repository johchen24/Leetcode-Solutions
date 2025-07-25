class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxPrice = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                maxPrice = max(maxPrice, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return maxPrice