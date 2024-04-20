class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

# Medium level problem
# 200 / 200 test cases passed.
# Status: Accepted
# Runtime: 33 ms
# Memory Usage: 12.8 MB
# Submitted: 0 minutes ago