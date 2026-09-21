class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        p=[0]*(len(prices))
        m=prices[0]
        for i in range(len(prices)):
            p[i]=prices[i]-m
            if prices[i]<m:
                m=prices[i]
        return max(p)