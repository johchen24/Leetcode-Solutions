class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        buy, sell = 0, 1
        while sell < len(prices):
            if prices[sell] < prices[sell - 1]:
                total += max(0, prices[sell - 1] - prices[buy])
                buy = sell
            sell += 1
        total += max(0, prices[sell - 1] - prices[buy])
        return total