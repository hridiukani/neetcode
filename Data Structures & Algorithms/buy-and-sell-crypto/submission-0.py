class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if max_pro<prices[j]-prices[i]:
                    max_pro=prices[j]-prices[i]
        return max_pro
