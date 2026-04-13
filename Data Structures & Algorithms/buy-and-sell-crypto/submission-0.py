class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow = 0
        profit = 0
        for fast in range(1, len(prices)):
            if prices[slow] < prices[fast]:
                profit = max (profit, prices[fast] - prices[slow])
            if prices[fast] < prices[slow]:
                slow = fast

        return profit