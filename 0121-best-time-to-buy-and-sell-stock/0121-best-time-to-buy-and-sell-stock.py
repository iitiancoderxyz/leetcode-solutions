class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mx=-float("inf")
        m=prices[0]
        for i in range(len(prices)):
            a=prices[i]-m
            if a>mx:
                mx=a
            if prices[i]<m:
                m=prices[i]
        return mx