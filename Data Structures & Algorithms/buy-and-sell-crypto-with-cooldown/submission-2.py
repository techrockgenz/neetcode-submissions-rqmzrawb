class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key(i, buying) val = max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i] # not buying is next step, because of cooldown
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i] # +2 because of cooldown, not buying is next
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)