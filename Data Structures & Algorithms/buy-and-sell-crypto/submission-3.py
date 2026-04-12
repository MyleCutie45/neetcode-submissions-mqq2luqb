class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        maxu = 0
        for r in range(1,len(prices)):
            profit = prices[r] - prices[l]
            maxu = max(profit,maxu)
            if prices[l] > prices[r]:
                l = r
        return maxu
