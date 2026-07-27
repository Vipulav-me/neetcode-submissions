class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        minbuy = prices[0]
        for i in prices:
            prof = max(prof,i-minbuy)
            minbuy = min(minbuy,i)
        return prof