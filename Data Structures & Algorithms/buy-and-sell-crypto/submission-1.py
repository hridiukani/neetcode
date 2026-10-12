class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff=0
        l=0
        r=1
        while r<len(prices):
            if prices[l]<=prices[r]:
                n=prices[r]-prices[l]
                diff=max(diff, n)
            else:
                l=r
            r+=1
        return diff

        