class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxp = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                prices[l] = prices[r]
                r+=1
            elif prices[l] <= prices[r]:
                maxp = max(prices[r]-prices[l],maxp)
                r+=1

        return maxp
        