class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxp = 0
        b = prices[0]
        for price in prices:
            b = min(price,b)
            mxp = max(mxp, price-b)
            print(b,mxp)
        return mxp
        