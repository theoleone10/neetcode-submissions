class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxP = 0
        minB = prices[0]
        for sell in prices:
            mxP = max(mxP, sell - minB)
            minB = min(minB, sell)
        return mxP
        